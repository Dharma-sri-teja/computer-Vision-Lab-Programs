import cv2
import numpy as np


image_path = input("Image path: ").strip()
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Could not read the image.")

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

cv2.imshow("Binary Image", binary)
cv2.imshow("Opening", opened)
cv2.waitKey(0)
cv2.destroyAllWindows()
