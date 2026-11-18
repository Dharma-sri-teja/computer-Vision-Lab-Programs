import cv2


image_path = input("Image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
if face_cascade.empty() or smile_cascade.empty():
    raise OSError("Could not load the Haar cascades.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(50, 50))
smile_count = 0
for x, y, width, height in faces:
    face_gray = gray[y:y + height, x:x + width]
    smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.7,
                                            minNeighbors=20, minSize=(20, 10))
    for sx, sy, sw, sh in smiles:
        cv2.rectangle(image, (x + sx, y + sy), (x + sx + sw, y + sy + sh),
                      (0, 255, 0), 2)
        smile_count += 1

print("Smile detections:", smile_count)
cv2.imshow("Smile Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
