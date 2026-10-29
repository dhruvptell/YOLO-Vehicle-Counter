import cv2
from ultralytics import YOLO

#loading pre-train yolo model
model = YOLO("yolov8n.pt")

image = "http://ultralytics.com/images/bus.jpg"

video = cv2.VideoCapture("traffic.mp4") #opens video
#cv extracts frames from the video
#yolo analyzes each frame


#checks whether the video opened successfully. 
if not video.isOpened():
    print("Error: Could not open traffic.mp4")
    exit()



while True:

    success, frame = video.read()
    #.read() reads next frame from video. "success" if true, was ran successfully.
    #frame is an image data for that frame, stored as NumPy array


    if not success:
        break

    results = model(frame)


    annotated_frame = results[0].plot()
    


    cv2.imshow("YOLOv8 Traffic Detection", annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break




video.release()
cv2.destroyALLWindows()

#results = model(image) #tells yolo to analyze the image

#results[0].show() #shows the result