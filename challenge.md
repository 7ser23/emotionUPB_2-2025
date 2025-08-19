# Emotion Detection Challenge 🚀


Welcome, Your goal is to get this facial emotion recognition project running.


## 📋 Instructions: Setup and Execution

Follow these steps carefully to set up your environment and run the code.

### Step 1: Clone the Project from GitHub

First, you need to download the project files from GitHub to your computer. This process is called "cloning." You have two easy options to do this.

#### Option A: Using the Command Line (Terminal)

1.  Open your terminal (on macOS/Linux) or Command Prompt/Git Bash (on Windows).
2.  Navigate to the directory where you want to store the project (e.g., `cd Documents/Projects`).
3.  Run the following command:
    ```bash
    git clone (https://github.com/7ser23/emotionUPB_2-2025.git)
    ```
4.  This will create a new folder named `emotionUPB_2-2025` containing all the project files.

#### Option B: Using PyCharm

1.  Open PyCharm and, on the Welcome screen, click **Get from VCS** (Version Control System). 
2.  If PyCharm is already open, go to **File** -> **New** -> **Project from Version Control**.
3.  In the URL field, paste the repository link:
    ```
    https://github.com/7ser23/emotionUPB_2-2025.git
    ```
4.  Choose a local directory where you want to save the project.
5.  Click **Clone**. PyCharm will download the project and set it up for you.

### 2. Project Structure

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

### 3. Create a Virtual Environment

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
### 4. Install Dependencies

Install all the required Python libraries using the requirements.txt file.
```bash
pip install -r requirements.txt
```

### 5. Run the Code
Now you can run the emotion detector on an image. The --image argument tells the script which image file to use.
### 6. Provide an analysis of the code and how it works
To submit your analysis and code for the upcoming challenges, you'll use a standard industry workflow called a Pull Request (PR).

#### Step 1: Fork the Repository 🍴

A "fork" is your personal copy of a repository that lives on your own GitHub account.

    Navigate to the main class repository on GitHub: https://github.com/7ser23/emotionUPB_2-2025

    In the top-right corner of the page, click the Fork button.

    GitHub will create a copy of the project under your own username (e.g., https://github.com/YourUsername/emotionUPB_2-2025).

#### Step 2: Clone Your Fork to Your Computer

Now, instead of cloning the original class repository, you'll clone the fork you just made.

    On your fork's GitHub page, click the green <> Code button and copy the HTTPS URL.

    In your terminal or using PyCharm, clone this URL. Make sure it has your username in it.

```bash
git clone https://github.com/YourUsername/emotionUPB_2-2025.git
```
#### Step 3: Create a New Branch 🌿

A branch is a separate workspace where you can safely work on new features (like your challenge solution) without affecting the main code.
1. Navigate into your newly cloned project directory.
```bash
cd emotionUPB_2-2025
```
2. Create a new branch and switch to it. Give it a descriptive name.
```bash
git checkout -b solve-David
```
#### Step 4: Complete and Commit Your Work

Now, modify the code to solve the challenge(s). As you complete parts of the work, "commit" your changes. A commit is a saved snapshot of your work.

1. Stage your changes (add them to the commit).
```bash
# This adds all modified files
git add .
```
2. Commit them with a clear message describing what you did.
```bash
git commit -m "Feat: Implement detection"
```
#### Step 5: Push Your Branch to Your Fork

Your branch and its commits only exist on your computer so far. You need to "push" them up to your forked repository on GitHub.
```bash
git push -u origin solve-challenge
```
#### Step 6: Open a Pull Request (PR) 📥

This is the final step where you "submit" your work for review.

1. Go to your forked repository on GitHub (https://github.com/YourUsername/emotionUPB_2-2025).

2. You should see a yellow banner prompting you to create a pull request from your new branch. Click the "Compare & pull request" button.

3. If you don't see the banner, go to the "Pull requests" tab and click "New pull request".

4. On the next page, make sure the settings are correct:
```bash
base repository: 7ser23/emotionUPB_2-2025

base: main

head repository: YourUsername/emotionUPB_2-2025

compare: solve-challenge
```
5. Give your pull request a clear title (e.g., "Solution for Webcam and Confidence Threshold Challenges") and write a brief description of the changes you made.

6. Click "Create pull request".