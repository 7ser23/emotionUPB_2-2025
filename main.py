import cv2
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
import argparse
from typing import List, Tuple

# Assuming ResEmoteNet class is in this path
from approach.ResEmoteNet import ResEmoteNet

# --- Constants and Configuration ---
# Set device (MPS for Apple Silicon, CUDA for Nvidia, otherwise CPU)
if torch.backends.mps.is_available():
    DEVICE = torch.device("mps")
elif torch.cuda.is_available():
    DEVICE = torch.device("cuda")
else:
    DEVICE = torch.device("cpu")

print(f"Using device: {DEVICE}")

# Emotion labels matching the model's output
EMOTIONS = ['happy', 'surprise', 'sad', 'anger', 'disgust', 'fear', 'neutral']
MODEL_PATH = 'train/fer2013_model.pth'
HAAR_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'


# --- Model and Preprocessing Setup ---

def load_emotion_model(model_path: str) -> torch.nn.Module:
    """Loads the pre-trained ResEmoteNet model."""
    model = ResEmoteNet().to(DEVICE)
    # Load the state dictionary, ensuring it's mapped to the correct device
    checkpoint = torch.load(model_path, map_location=DEVICE)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.eval()
    return model


def get_image_transform() -> transforms.Compose:
    """Defines the image transformation pipeline for the model."""
    return transforms.Compose([
        transforms.Resize((64, 64)),
        transforms.Grayscale(num_output_channels=3),  # Model expects 3 channels
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])


# --- Core Functions ---

def predict_emotion(model: torch.nn.Module, image: Image.Image, transform: transforms.Compose) -> Tuple[
    str, np.ndarray]:
    """Predicts the emotion from a single face image."""
    img_tensor = transform(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(img_tensor)
        probabilities = F.softmax(outputs, dim=1)

    scores = probabilities.cpu().numpy().flatten()
    predicted_emotion_idx = np.argmax(scores)
    predicted_emotion = EMOTIONS[predicted_emotion_idx]
    return predicted_emotion, scores


def process_image(image_path: str, model: torch.nn.Module, transform: transforms.Compose):
    """Loads an image, detects faces, predicts emotions, and displays the result."""
    try:
        # Read image with OpenCV for drawing and processing
        image_cv2 = cv2.imread(image_path)
        if image_cv2 is None:
            raise FileNotFoundError(f"Could not read image from path: {image_path}")

        # Convert from BGR (OpenCV default) to RGB for PIL and face detection
        image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
        gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2GRAY)

        # Load Haar Cascade for face detection
        face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))

        if len(faces) == 0:
            print("No faces detected in the image.")
            return

        print(f"Detected {len(faces)} face(s).")

        # Convert the full image to PIL format once
        image_pil = Image.fromarray(image_rgb)

        # Process each detected face
        for (x, y, w, h) in faces:
            # Draw a bounding box around the face
            cv2.rectangle(image_cv2, (x, y), (x + w, y + h), (50, 205, 50), 2)

            # Crop the face region from the PIL image for emotion detection
            face_image = image_pil.crop((x, y, x + w, y + h))

            # Get emotion prediction
            emotion, scores = predict_emotion(model, face_image, transform)

            # --- Display Results ---
            print(f"\nEmotion for face at ({x}, {y}): {emotion}")
            for label, score in zip(EMOTIONS, scores):
                print(f"  - {label.capitalize()}: {score:.2%}")

            # Smartly position the text above the bounding box
            text_y = y - 10 if y - 10 > 10 else y + h + 20
            cv2.putText(image_cv2, emotion, (x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (50, 205, 50), 2)

        # Show the final image
        cv2.imshow("Emotion Detection", image_cv2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main Execution ---

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Detect faces and predict emotions in an image.")
    parser.add_argument("--image", type=str, required=True, help="Path to the input image.")
    args = parser.parse_args()

    # Load model and transforms
    emotion_model = load_emotion_model(MODEL_PATH)
    image_transform = get_image_transform()

    # Process the specified image
    process_image(args.image, emotion_model, image_transform)