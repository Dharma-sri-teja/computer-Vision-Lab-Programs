import cv2
import numpy as np


width = int(input("Image width: "))
height = int(input("Image height: "))
if width <= 0 or height <= 0:
    raise ValueError("Width and height must be positive.")

image = np.full((height, width, 3), 255, dtype=np.uint8)
center_x = int(input("Circle center x: "))
center_y = int(input("Circle center y: "))
radius = int(input("Circle radius: "))
if radius <= 0:
    raise ValueError("Radius must be positive.")
cv2.circle(image, (center_x, center_y), radius, (255, 0, 0), 2)

cv2.imshow("Circle", image)
cv2.imwrite("q34_circle.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
