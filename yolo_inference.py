from ultralytics import YOLO

model = YOLO("yolov8x")

results = model.predict("input/input_video_short.mp4", save=True, project="runs/")

for box in results[0].boxes:
    print(box)
