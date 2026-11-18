import cv2


image_path = input("Image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
if face_cascade.empty():
    raise OSError("Could not load the Haar face cascade.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5,
                                      minSize=(30, 30))
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

print("Faces detected:", len(faces))
cv2.imshow("Face Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
