import cv2


image_path = input("Image path: ").strip()
threshold_value = int(input("Threshold value (0-255): "))
max_value = int(input("Maximum output value [255]: ") or "255")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Could not read the image.")
if not 0 <= threshold_value <= 255 or not 1 <= max_value <= 255:
    raise ValueError("Threshold and maximum values must be between 0 and 255.")

_, segmented = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)
cv2.imshow("Grayscale Image", image)
cv2.imshow("Threshold Segmentation", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
