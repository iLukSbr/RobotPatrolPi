import cv2
import numpy as np

print(cv2.__version__)  # Check OpenCV version

# Define the dictionary (type of marker) to use
aruco_dict = cv2.aruco.Dictionary(cv2.aruco.DICT_4X4_50)

# Set up the parameters for marker generation
parameters = cv2.aruco.DetectorParameters_create()

# Create the marker image
marker_id = 23  # ID of the marker
marker_size = 200  # Marker size in pixels
marker_image = cv2.aruco.drawMarker(aruco_dict, marker_id, marker_size)

# Save the marker image
cv2.imwrite("aruco_marker_23.png", marker_image)

# Optionally, display the marker image
cv2.imshow("AR Marker", marker_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
