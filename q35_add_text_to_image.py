import cv2


image_path = input("Image path: ").strip()
text = input("Text to display: ")
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

x = int(input("Text x-coordinate: "))
y = int(input("Text y-coordinate: "))
cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow("Text on Image", image)
cv2.imwrite("q35_text_image.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
