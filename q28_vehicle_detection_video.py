import cv2


video_path = input("Video path: ").strip()
capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise OSError("Could not open the video.")

# Background subtraction highlights moving objects; detections need not be vehicles.
background = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=40)
while True:
    ok, frame = capture.read()
    if not ok:
        break

    mask = background.apply(frame)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,
                            cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 800:
            continue
        x, y, width, height = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        cv2.putText(frame, "Moving object", (x, max(20, y - 5)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Moving Vehicle/Object Detection", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

capture.release()
cv2.destroyAllWindows()
