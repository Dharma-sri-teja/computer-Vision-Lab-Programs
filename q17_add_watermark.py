import cv2


image_path = input("Image path: ").strip()
text = input("Watermark text: ")
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError("Could not read the image.")

watermark = image.copy()
height, width = image.shape[:2]
cv2.putText(watermark, text, (20, height - 25), cv2.FONT_HERSHEY_SIMPLEX,
            max(0.6, width / 1000), (255, 255, 255), 2, cv2.LINE_AA)
result = cv2.addWeighted(watermark, 0.35, image, 0.65, 0)

cv2.imshow("Watermarked Image", result)
cv2.imwrite("q17_watermarked.png", result)
print("Saved as q17_watermarked.png")
cv2.waitKey(0)
cv2.destroyAllWindows()
