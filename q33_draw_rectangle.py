import cv2
import numpy as np


width = int(input("Image width: "))
height = int(input("Image height: "))
if width <= 0 or height <= 0:
    raise ValueError("Width and height must be positive.")

image = np.full((height, width, 3), 255, dtype=np.uint8)
x1 = int(input("Rectangle top-left x: "))
y1 = int(input("Rectangle top-left y: "))
x2 = int(input("Rectangle bottom-right x: "))
y2 = int(input("Rectangle bottom-right y: "))
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow("Rectangle", image)
cv2.imwrite("q33_rectangle.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
