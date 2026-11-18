import cv2


image_path = input("Image path: ").strip()
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
edges = cv2.convertScaleAbs(cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5,
                                             cv2.convertScaleAbs(sobel_y), 0.5, 0))

cv2.imshow("Original", image)
cv2.imshow("Sobel X", cv2.convertScaleAbs(sobel_x))
cv2.imshow("Sobel Y", cv2.convertScaleAbs(sobel_y))
cv2.imshow("Sobel Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
