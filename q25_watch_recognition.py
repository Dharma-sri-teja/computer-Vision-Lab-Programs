import cv2


scene_path = input("Image containing the watch: ").strip()
template_path = input("Image/template containing only the watch: ").strip()
scene = cv2.imread(scene_path)
template = cv2.imread(template_path)
if scene is None or template is None:
    raise FileNotFoundError("Could not read the scene or watch template.")

scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
if template_gray.shape[0] > scene_gray.shape[0] or template_gray.shape[1] > scene_gray.shape[1]:
    raise ValueError("The watch template must be smaller than the scene image.")

scores = cv2.matchTemplate(scene_gray, template_gray, cv2.TM_CCOEFF_NORMED)
_, score, _, location = cv2.minMaxLoc(scores)
threshold = 0.65
if score >= threshold:
    h, w = template_gray.shape
    cv2.rectangle(scene, location, (location[0] + w, location[1] + h),
                  (0, 255, 0), 2)
    print("Watch found. Match score:", round(score, 3))
else:
    print("No confident watch match. Best score:", round(score, 3))

cv2.imshow("Watch Recognition", scene)
cv2.waitKey(0)
cv2.destroyAllWindows()
