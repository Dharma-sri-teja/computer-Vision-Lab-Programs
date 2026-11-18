import cv2


image_path = input("Image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
if face_cascade.empty() or eye_cascade.empty():
    raise OSError("Could not load the Haar cascades.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(30, 30))
eye_count = 0
for x, y, width, height in faces:
    face_gray = gray[y:y + height, x:x + width]
    face_color = image[y:y + height, x:x + width]
    eyes = eye_cascade.detectMultiScale(face_gray, 1.1, 5, minSize=(10, 10))
    for ex, ey, ew, eh in eyes:
        cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
        eye_count += 1

print("Eyes detected:", eye_count)
cv2.imshow("Eye Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
