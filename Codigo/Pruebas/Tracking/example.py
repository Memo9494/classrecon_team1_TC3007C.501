from ultralytics import YOLO
import cv2

# Load a pretrained YOLOv8n-pose Pose model
model = YOLO('yolov8n-pose.pt')

cap = cv2.VideoCapture(0)

# Run inference on an image
results = model('bus.jpg')  # results list

# View results
for r in results:
    print(r.keypoints)  # print the Keypoints object containing the detected keypoints