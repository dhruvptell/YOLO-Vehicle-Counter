
# YOLOv8 Vehicle Counter

## Overview

A computer vision project developed using Python, YOLOv8, and OpenCV.

The application processes traffic videos, detects vehicles, tracks them across frames, and counts vehicles crossing a designated line.

## Features

- Detect cars, trucks, buses, and motorcycles.
- Track vehicles across video frames using ByteTrack.
- Assign tracking IDs to detected vehicles.
- Count vehicles crossing a horizontal line.
- Display bounding boxes, tracking information, and vehicle counts.

## Technologies Used

- Python
- Ultralytics YOLOv8
- OpenCV
- ByteTrack

## How to Run

1. Install Python 3.11.
2. Download or clone this repository.
3. Install the required packages:

   `python -m pip install -r requirements.txt`

4. Add a traffic video named `traffic.mp4` to the project folder.
5. Run the application:

   `python main.py`

6. Press Q to stop the video.

Note: The sample traffic video is not included in this repository.

## How It Works

1. OpenCV reads the traffic video frame by frame.
2. YOLOv8 detects vehicles and predicts their bounding boxes.
3. ByteTrack associates vehicles across consecutive frames using tracking IDs.
4. The program calculates the center of each vehicle's bounding box.
5. When a tracked vehicle crosses the counting line, the counter increases.

## Limitations

- Vehicle counts depend on detection and tracking accuracy.
- Tracking ID changes may cause counting errors.
- The current counting logic uses a horizontal line.

## Future Improvements

- Improve vehicle-counting accuracy.
- Support vertical and customizable counting lines.
- Export vehicle statistics to CSV.
- Evaluate model performance and processing speed.
- Explore depth estimation and vision-language models.
