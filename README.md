# 🤖 Stickman Tracker Recorder

**Stickman Tracker Recorder** is a real-time human pose tracking and recording system built using **Python 🐍, OpenCV 🎥, and MediaPipe 🧠**. The application detects human body landmarks from a webcam and converts movements into a **stickman skeleton animation 🕺**.

Instead of recording the original camera video, the system records **only the stickman movement on a black background ⚫**, making it useful for **motion analysis, animation reference, posture tracking, and gesture visualization**.

---

# ✨ Features

✅ Real-time **human pose detection**
✅ Converts body movements into a **stickman skeleton**
✅ Records **stickman animation instead of camera footage**
✅ Automatically creates a **recordings folder 📂**
✅ Auto-saves videos (`stickman_1.mp4`, `stickman_2.mp4`, ...)
✅ Runs in **fullscreen mode 🖥️**
✅ Press **ENTER ⏎ to stop recording**
✅ Filters unstable tracking by requiring **shoulders and hips visibility**

---

# 📂 Project Structure

```
Stickman Tracker Recorder
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

📁 The **recordings folder** is automatically created when the program runs.

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```
git clone https://github.com/rsamwilson2323-cloud/Stickman-Tracker-Recorder.git
cd Stickman-Tracker-Recorder
```

## 2️⃣ Install dependencies

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

Run the program using:

```
python "stickman tracker recorder.py"
```

📷 The webcam will start and detect body movements.

The program will:

* Track your **body pose**
* Convert it into a **stickman skeleton**
* Record the stickman animation automatically

To stop recording:

**Press ENTER ⏎**

The video will be saved inside the **recordings folder 📁**.

---

# 🧠 How It Works

1️⃣ The webcam captures live video 🎥
2️⃣ **MediaPipe Pose** detects body landmarks (shoulders, elbows, hips, knees, etc.)
3️⃣ These landmarks are connected to form a **stickman skeleton 🕺**
4️⃣ The skeleton is drawn on:

* the preview camera frame
* a black background used for recording

5️⃣ The stickman animation is saved as an **MP4 video 🎬**

---

# 🎯 Applications

📊 Motion analysis
🎨 Animation reference creation
🏋️ Sports posture tracking
🤖 Human movement research
🕹️ Gesture-based interaction systems

---

# 👨‍💻 Author

**Sam Wilson**

📧 Email: [rsamwilson2323@gmail.com](mailto:rsamwilson2323@gmail.com)
🌐 GitHub: https://github.com/rsamwilson2323-cloud
💼 LinkedIn: https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the **MIT License**.
Feel free to use, modify, and distribute this project.
