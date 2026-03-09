# 🤖 Stickman Tracker Recorder

Stickman Tracker Recorder is a real-time **human pose tracking and recording system** built using **Python 🐍, OpenCV 🎥, and MediaPipe 🧠**.

The program detects human body landmarks from a webcam and converts body movements into a **stickman skeleton animation 🕺**. Instead of recording the original camera video, the system records only the **stickman movement on a black background**, making it useful for motion analysis and animation reference.

---

# ✨ Features

✅ Real-time **pose detection**
✅ Converts body movement into a **stickman skeleton**
✅ Records **stickman animation instead of webcam video**
✅ Automatically creates a **recordings folder 📂**
✅ Saves videos sequentially (`stickman_1.mp4`, `stickman_2.mp4`, ...)
✅ **Fullscreen display 🖥️**
✅ Press **ENTER ⏎ to stop recording**

---

# 📂 Project Structure

```
Stickman-Tracker-Recorder
│
├── stickman tracker recorder.py
├── README.md
├── requirements.txt
├── LICENSE
│
└── recordings
      ├── stickman_1.mp4
      ├── stickman_2.mp4
      └── stickman_3.mp4
```

The **recordings folder** will be created automatically when the program runs.

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/rsamwilson2323-cloud/Stickman-Tracker-Recorder.git
cd Stickman-Tracker-Recorder
```

### 2️⃣ Install Required Libraries

```
pip install -r requirements.txt
```

---

# 📦 Requirements

```
opencv-python
mediapipe
numpy
```

---

# ▶️ Usage

Run the program:

```
python "stickman tracker recorder.py"
```

The webcam will open and detect body movements.

The program will:

• Track your **body pose**
• Convert it into a **stickman skeleton**
• Record the stickman animation automatically

To stop recording:

**Press ENTER ⏎**

The video will be saved in the **recordings folder 📁**.

---

# 🧠 How It Works

1️⃣ The webcam captures live video 🎥
2️⃣ **MediaPipe Pose** detects body landmarks (shoulders, elbows, hips, knees, etc.)
3️⃣ These landmarks are connected to create a **stickman skeleton**
4️⃣ The skeleton is drawn on the preview screen and on a black background
5️⃣ The stickman animation is saved as an **MP4 video 🎬**

---

# 🎯 Applications

🎨 Animation reference
🏃 Motion analysis
🏋️ Sports posture tracking
🤖 Human movement research
🕹️ Gesture visualization

---

# 👨‍💻 Author

Sam Wilson

🌐 GitHub: 
https://github.com/rsamwilson2323-cloud

💼 LinkedIn: 
https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the **MIT License**.
