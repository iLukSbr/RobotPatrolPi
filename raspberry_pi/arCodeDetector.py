from dataclasses import dataclass
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import os

os.environ["OPENCV_GUI"] = "gtk"

# Initialize the camera (use your Logitech 720p webcam)
cap = cv2.VideoCapture(0)  # Adjust the camera index if necessary (0 is usually the default)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Parameters
code_size = 5.0  # Real-world size of the QR code in centimeters (you need to set this)
focal_length = 500  # Estimated focal length (you may need to adjust this value)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Decode the AR codes (or QR codes)
    decoded_objects = decode(frame)

    for obj in decoded_objects:
        # Draw a rectangle around the detected code
        points = obj.polygon
        if len(points) == 4:
            points = [(int(point.x), int(point.y)) for point in points]
            cv2.polylines(frame, [np.array(points)], True, (0, 0, 255), 2)
        else:
            # Handle more complex shapes (optional)
            pass

        # Display the data decoded from the AR code
        barcode_data = obj.data.decode('utf-8')
        barcode_type = obj.type
        print(f"Decoded {barcode_type}: {barcode_data}")

        # Get the width of the QR code in pixels (we assume the QR code is a square)
        width = int(np.linalg.norm(np.array(points[0]) - np.array(points[1])))
        
        # Estimate the distance using the formula
        distance = (focal_length * code_size) / width

        # Display the decoded text on the image
        cv2.putText(frame, f"{barcode_data} - Dist: {distance:.2f} cm", 
                    (points[0][0], points[0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Show the resulting frame
    cv2.imshow('AR Code Scanner', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
