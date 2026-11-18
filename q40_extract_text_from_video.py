import cv2


video_path = input("Video path: ").strip()
output_path = input("Text output file [q40_video_text.txt]: ").strip()
output_path = output_path or "q40_video_text.txt"
frame_interval = int(input("Process every Nth frame [15]: ") or "15")
if frame_interval < 1:
    raise ValueError("Frame interval must be at least 1.")

try:
    import pytesseract
except ImportError as error:
    raise SystemExit("Install OCR dependency with: pip install pytesseract") from error

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise OSError("Could not open the video.")
fps = capture.get(cv2.CAP_PROP_FPS)
fps = fps if fps > 0 else 25
frame_number = 0
results = []
while True:
    ok, frame = capture.read()
    if not ok:
        break
    if frame_number % frame_interval == 0:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray).strip()
        if text:
            timestamp = frame_number / fps
            results.append("Time {:.2f}s:\n{}".format(timestamp, text))
            print(results[-1])
    frame_number += 1
capture.release()

with open(output_path, "w", encoding="utf-8") as output_file:
    output_file.write("\n\n".join(results))
print("Saved extracted text to", output_path)
