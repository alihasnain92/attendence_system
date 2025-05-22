import cv2
import os

def capture_images(name, roll, num_images=10, save_path='dataset'):
    folder_name = f"{name}_{roll}"
    os.makedirs(f"{save_path}/{folder_name}", exist_ok=True)
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            filename = f"{save_path}/{folder_name}/{count}.jpg"
            cv2.imwrite(filename, face)
            count += 1
            cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        cv2.imshow("Capturing Images", frame)
        if cv2.waitKey(1) == ord('q') or count >= num_images:
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captured {count} images for {name} ({roll})")
