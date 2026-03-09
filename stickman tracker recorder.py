import cv2
import mediapipe as mp
import numpy as np
import os

# --------------------
# Mediapipe Pose Setup
# --------------------
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.6, min_tracking_confidence=0.6)

# --------------------
# Fullscreen Window
# --------------------
cv2.namedWindow("Stickman Studio", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Stickman Studio", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

cap = cv2.VideoCapture(0)

recording = True
writer = None

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
connections = mp_pose.POSE_CONNECTIONS

# -------------------
# Folder for recordings (auto create in project folder)
# -------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
save_folder = os.path.join(base_dir, "recordings")
os.makedirs(save_folder, exist_ok=True)

# -------------------
# Auto-number filename
# -------------------
def get_next_filename():
    n = 1
    while True:
        name = os.path.join(save_folder, f"stickman_{n}.mp4")
        if not os.path.exists(name):
            return name
        n += 1

# -------------------
# Draw Stickman
# -------------------
def draw_stickman(landmarks, frame_or_bg, vis_th=0.6):
    h, w, _ = frame_or_bg.shape

    # Require shoulders and hips visible
    required = [11, 12, 23, 24]
    for i in required:
        if landmarks[i].visibility < 0.55:
            return frame_or_bg

    # Draw joints
    for lm in landmarks:
        if lm.visibility > vis_th:
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame_or_bg, (cx, cy), 4, (0, 0, 255), -1)

    # Draw bones
    for c in connections:
        a = landmarks[c[0]]
        b = landmarks[c[1]]

        if a.visibility > vis_th and b.visibility > vis_th:
            x1, y1 = int(a.x * w), int(a.y * h)
            x2, y2 = int(b.x * w), int(b.y * h)
            cv2.line(frame_or_bg, (x1, y1), (x2, y2), (0, 0, 255), 3)

    return frame_or_bg

# -------------------
# Initialize Video Writer
# -------------------
ret, frame = cap.read()

if not ret:
    print("Camera not detected!")
    cap.release()
    exit()

h, w, _ = frame.shape
filename = get_next_filename()

writer = cv2.VideoWriter(filename, fourcc, 30, (w, h))

print("Recording started:", filename)

# -------------------
# MAIN LOOP
# -------------------
while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    # Black background for recording
    black_bg = np.zeros((h, w, 3), dtype=np.uint8)

    # Pose detection
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(rgb)

    preview = frame.copy()

    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark

        preview = draw_stickman(landmarks, preview)
        black_bg = draw_stickman(landmarks, black_bg)

    cv2.imshow("Stickman Studio", preview)

    # Save stickman animation
    writer.write(black_bg)

    # Exit using ENTER key
    if cv2.waitKey(1) == 13:
        break

# -------------------
# Cleanup
# -------------------
cap.release()
writer.release()
cv2.destroyAllWindows()

print("Recording saved:", filename)
