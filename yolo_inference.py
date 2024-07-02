from ultralytics import YOLO

# model = YOLO("yolov8x")
model = YOLO("models/temp/best.pt")

results = model.predict("input/input_video.mp4", save=True, project="runs/")

for box in results[0].boxes:
    print(box)


# 11:39
