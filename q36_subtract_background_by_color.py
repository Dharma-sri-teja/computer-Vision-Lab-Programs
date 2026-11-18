import cv2
import numpy as np


image_path = input("Image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

print("Enter the background color bounds in HSV (H: 0-179, S/V: 0-255).")
lower = np.array([int(input("Lower H: ")), int(input("Lower S: ")),
                  int(input("Lower V: "))], dtype=np.uint8)
upper = np.array([int(input("Upper H: ")), int(input("Upper S: ")),
                  int(input("Upper V: "))], dtype=np.uint8)
if np.any(lower > upper):
    raise ValueError("Each lower HSV bound must be less than or equal to its upper bound.")

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
background_mask = cv2.inRange(hsv, lower, upper)
result = image.copy()
result[background_mask > 0] = (255, 255, 255)

cv2.imshow("Background Mask", background_mask)
cv2.imshow("Background Subtracted", result)
cv2.imwrite("q36_background_subtracted.png", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
