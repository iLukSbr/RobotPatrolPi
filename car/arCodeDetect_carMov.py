#Car Movement
from time import sleep
import RPi.GPIO as GPIO
import time

#Camera
from dataclasses import dataclass
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import os

points =0
# ------------------------------- Camera Set up -------------------------------
os.environ["OPENCV_GUI"] = "gtk"

# Initialize the camera (use your Logitech 720p webcam)
cap = cv2.VideoCapture(0)  # Adjust the camera index if necessary (0 is usually the default)

if not cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Parameters (we MAY change these later)
code_size = 5.0  # Real-world size of the QR code in centimeters 
focal_length = 500  # Estimated focal length 

# ------------------------------- Camera Set up -------------------------------

GPIO.setwarnings(False)

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13

#Time to wait
WAIT = 3
RIGHTTURN = 0.4
LEFTTURN = 0.42
FORWARDSIDES = 0.4

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)

GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(en_b, GPIO.OUT)

q = GPIO.PWM(en_a, 100)
p = GPIO.PWM(en_b, 100)
p.start(30)
q.start(30)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)

try:
    # Create Infinite loop to read user input
    while True:

        # Clear buffer by reading a few frames before processing
        for _ in range(5):  
            cap.grab()  # Grab (discard) a few frames to ensure a fresh one

        p.start(50) #Increases speed
        q.start(50)
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            continue  # Skip this iteration and try again

        # Decode the AR codes (or QR codes)
        decoded_objects = decode(frame)
        last_qr_code = None

        if decoded_objects:
            obj = decoded_objects[0] 
            points = obj.polygon 
            last_qr_code = decoded_objects[0].data.decode('utf-8')
            print(f"Detected QR Code: {last_qr_code}")
        else:
            if last_qr_code is not None:
                print("QR Code lost, resetting detection.")
            last_qr_code = None  # Force reset
            points = None

        
        # Draw a rectangle around the detected code
        
        #if len(points) == 4:
        #    points = [(int(point.x), int(point.y)) for point in points]
        #    cv2.polylines(frame, [np.array(points)], True, (0, 0, 255), 2)
        #else:
        #    # Handle more complex shapes (optional)
        #    pass

            
        if points:
            # Get the width of the QR code in pixels (we assume the QR code is a square)
            width = int(np.linalg.norm(np.array(points[0]) - np.array(points[1])))
            
            # Estimate the distance using the formula
            distance = (focal_length * code_size) / width
        else:
            distance = 1000

        # Display the decoded text on the image
        # cv2.putText(frame, f"{barcode_data} - Dist: {distance:.2f} cm", 
        #             (points[0][0], points[0][1] - 10),
        #            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        if distance < 15:
            if last_qr_code == 'Q3':
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in4, GPIO.LOW)
                GPIO.output(in3, GPIO.HIGH)
                time.sleep(WAIT)
                print('Back')

            elif last_qr_code == 'Q1':
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
                GPIO.output(in3, GPIO.HIGH)
                time.sleep(WAIT)
                print('Right')
                time.sleep(RIGHTTURN)
                # Stop the car after performing the turn
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)

            elif last_qr_code == 'Q2':
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                GPIO.output(in4, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                time.sleep(WAIT)
                print('Left')
                time.sleep(LEFTTURN)
                # Stop the car after performing the turn
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)

            elif last_qr_code == 'Q4':
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in4, GPIO.LOW)
                GPIO.output(in3, GPIO.LOW)
                print('Stop')
                break
            
            else :
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                GPIO.output(in4, GPIO.HIGH)
                GPIO.output(in3, GPIO.LOW)
                print("Forward")
            
        

        # Show the resulting frame
        #cv2.imshow('AR Code Scanner', frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Get user Input
        #user_input = input("Enter command (w/s/a/d for control, c to stop): ")

        

            
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

#except KeyboardInterrupt:
#    print("Keyboard Interrupt detected. Exiting...")



finally:
    # Reset GPIO settings
    GPIO.cleanup()
    print("GPIO Clean up")

    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()
    


