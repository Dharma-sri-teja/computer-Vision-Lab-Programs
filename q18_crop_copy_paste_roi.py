import cv2


image_path = input("Source image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

x, y, width, height = cv2.selectROI("Select ROI", image, showCrosshair=True)
cv2.destroyWindow("Select ROI")
if width == 0 or height == 0:
    raise ValueError("No region was selected.")

roi = image[y:y + height, x:x + width].copy()
result = image.copy()
max_x = result.shape[1] - width
max_y = result.shape[0] - height
paste_x = min(0, max_x)
paste_y = min(0, max_y)
result[paste_y:paste_y + height, paste_x:paste_x + width] = roi

cv2.imshow("Cropped ROI", roi)
cv2.imshow("Image with copied ROI pasted at top-left", result)
cv2.imwrite("q18_roi.png", roi)
cv2.imwrite("q18_roi_pasted.png", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
