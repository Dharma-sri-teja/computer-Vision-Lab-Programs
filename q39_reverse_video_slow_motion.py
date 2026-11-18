import cv2


video_path = input("Input video path: ").strip()
output_path = input("Output video path [q39_reverse_slow.avi]: ").strip()
output_path = output_path or "q39_reverse_slow.avi"
slow_factor = int(input("Slow-motion factor [2]: ") or "2")
if slow_factor < 1:
    raise ValueError("Slow-motion factor must be at least 1.")

capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    raise OSError("Could not open the video.")
fps = capture.get(cv2.CAP_PROP_FPS)
frames = []
while True:
    ok, frame = capture.read()
    if not ok:
        break
    frames.append(frame)
capture.release()
if not frames:
    raise ValueError("The video contains no readable frames.")

height, width = frames[0].shape[:2]
writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"XVID"),
                         fps if fps > 0 else 25, (width, height))
if not writer.isOpened():
    raise OSError("Could not create the output video.")
for frame in reversed(frames):
    for _ in range(slow_factor):
        writer.write(frame)
writer.release()
print("Saved reverse slow-motion video to", output_path)
