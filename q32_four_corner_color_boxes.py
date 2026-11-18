import cv2
import numpy as np


width = int(input("Image width: "))
height = int(input("Image height: "))
if width <= 0 or height <= 0:
    raise ValueError("Width and height must be positive.")

image = np.full((height, width, 3), 255, dtype=np.uint8)
box_width = max(1, width // 10)
box_height = max(1, height // 10)
image[:box_height, :box_width] = (0, 0, 0)  # Black, top-left
image[:box_height, width - box_width:] = (255, 0, 0)  # Blue, top-right (BGR)
image[height - box_height:, :box_width] = (0, 255, 0)  # Green, bottom-left
image[height - box_height:, width - box_width:] = (0, 0, 255)  # Red, bottom-right

cv2.imshow("Four Colored Corner Boxes", image)
cv2.imwrite("q32_corner_boxes.png", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
