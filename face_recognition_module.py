
import face_recognition
import cv2
import os
import json
from mark_attendance import mark_attendance_once

def load_known_faces(path="dataset"):
    with open("users.json", "r") as f:
        users = json.load(f)

    known_encodings = []
    known_names = []
    known_rolls = []

    for user in users:
        folder = user["image_folder"]
        name = user["name"]
        roll = user["roll"]
        if not os.path.exists(folder):
            continue
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            img = face_recognition.load_image_file(file_path)
            encoding = face_recognition.face_encodings(img)
            if encoding:
                known_encodings.append(encoding[0])
                known_names.append(name)
                known_rolls.append(roll)

    return known_encodings, known_names, known_rolls

def recognize_faces(known_encodings, known_names, known_rolls):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        print("❌ Failed to access webcam.")
        return


    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for encoding, face in zip(encodings, faces):
            matches = face_recognition.compare_faces(known_encodings, encoding)
            name = "Unknown"
            roll = "Unknown"

            if True in matches:
                index = matches.index(True)
                name = known_names[index]
                roll = known_rolls[index]
            else:
                continue  # Skip unknowns

            # Call attendance marking and interpret result
            from datetime import datetime
            from tkinter import messagebox
            today = datetime.now().strftime("%Y-%m-%d")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            import json
            try:
                with open("attendance/attendance.json", "r") as f:
                    data = json.load(f)
            except:
                data = []

            already_marked = any(entry["name"] == name and entry["roll"] == roll and entry["timestamp"].startswith(today) for entry in data)

            if already_marked:
                messagebox.showinfo("Attendance", f"⚠️ Attendance already marked today for {name} ({roll})")
                cap.release()
                cv2.destroyAllWindows()
                return

            mark_attendance_once(name, roll)
            messagebox.showinfo("Attendance", f"✅ Attendance marked for {name} ({roll}) at {timestamp}")
            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
