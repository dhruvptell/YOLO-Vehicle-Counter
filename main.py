import cv2
from ultralytics import YOLO

#loading pre-train yolo model
model = YOLO("yolov8n.pt")

image = "http://ultralytics.com/images/bus.jpg"

video = cv2.VideoCapture("traffic.mp4") #opens video
#cv extracts frames from the video
#yolo analyzes each frame


#gets the height of the video
#video.get() gets property of video
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#put the coutning line halfway down
line_y = height // 2


#checks whether the video opened successfully. 
if not video.isOpened():
    print("Error: Could not open traffic.mp4")
    exit()


previous_y = {} #remember each vehciles's previous position

counted_ids = set() #rememebrs which vechile have already been counted

vehicle_count = 0 #total vehicles that crossed the line


while True:




    success, frame = video.read()
    #.read() reads next frame from video. "success" if true, was ran successfully.
    #frame is an image data for that frame, stored as NumPy array


    if not success:
        break

    #results = model(frame)

    # .track tracks object
    results = model.track(frame, #image
                          persist= True, #keeps tracking info
                          tracker="bytetrack.yaml",
                          classes = [2, 3, 5, 7] #class id represent cars, motercycles, buses etc
    )

    

    boxes = results[0].boxes
    if boxes is not None and boxes.is_track:

        # gets the ids

        ids = boxes.id.int().cpu().tolist()

        # Get bounding box coordinates
        coordinates = boxes.xyxy.cpu().tolist()

          # Loop through each detected vehicle
        for track_id, (x1, y1, x2, y2) in zip(ids, coordinates):

            # Find the vehicle's vertical center
            center_y = (y1 + y2) / 2

            # Retrieve its previous position
            old_y = previous_y.get(track_id)

            # Only count vehicles we haven't counted
            if old_y is not None and track_id not in counted_ids:

                # Check if the vehicle crossed the yellow line
                crossed = (
                    (old_y < line_y <= center_y) or
                    (old_y > line_y >= center_y)
                )

                if crossed:

                    # Increase vehicle count
                    vehicle_count += 1

                    # Remember this vehicle
                    counted_ids.add(track_id)

                    print("Vehicles counted:", vehicle_count)

            # Save current position for the next frame
            previous_y[track_id] = center_y







        print("Tracking IDs:", boxes.id.int().cpu().tolist())

    #draws bounding boxes
    annotated_frame = results[0].plot()

    cv2.line( #draws a line on image

        annotated_frame,
        (0, line_y),
        (annotated_frame.shape[1], line_y),
        (0, 255, 255),
        2
    )

    # Display total vehicles counted
    cv2.putText(
        annotated_frame,
        f"Vehicles crossed: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )
    


    cv2.imshow("YOLOv8 Traffic Detection", annotated_frame)


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



video.release()
cv2.destroyAllWindows()

#results = model(image) #tells yolo to analyze the image

#results[0].show() #shows the result