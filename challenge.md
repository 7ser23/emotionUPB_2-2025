# Emotion Detection Challenge 🚀

Welcome, students! Your goal is to get this facial emotion recognition project running and then extend its capabilities.



## 📋 Instructions: Setup and Execution

Follow these steps carefully to set up your environment and run the code.

### 1. Project Structure

First, make sure your project files are organized correctly. The script expects the model and other files to be in specific locations.
```bash
emotionUPB/
├── approach/
│   └── ResEmoteNet.py      # The Python file defining the model architecture
├── train/
│   └── fer2013_model.pth   # The pre-trained model weights
├── images/
│   └── test_image.jpg      # An image you want to test
├── main.py                 # The main script you will run
├── requirements.txt        # The list of Python packages needed
└── README.md
```
**Note:** Sergio will provide you with the `approach/ResEmoteNet.py` and `train/fer2013_model.pth` files.

### 2. Create a Virtual Environment

It's best practice to use a virtual environment to keep project dependencies isolated.

```bash
# Create a virtual environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies

Install all the required Python libraries using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 4. Run the Code
Now you can run the emotion detector on an image. The --image argument tells the script which image file to use.
### 5. Provide an analysis of the code and how it works