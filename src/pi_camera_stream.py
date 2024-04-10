from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import cv2

# Define the size of the video stream
size = (320, 240)

# Parameters for JPEG encoding
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]


def get_encoded_bytes_for_frame(frame):
    if frame is None:
        return None

    # Ensure frame is in BGR color space
    if len(frame.shape) == 3 and frame.shape[2] == 3:
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Convert frame to a valid format for cv2.imencode
    frame = np.asarray(frame)

    # Encode frame to JPEG format
    result, encoded_image = cv2.imencode('.jpg', frame, encode_param)
    return encoded_image.tostring() if result else None

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

def setup_camera():
    camera = PiCamera()
    camera.resolution = size
    camera.rotation = 0
    return camera

def start_stream(camera):
    image_storage = PiRGBArray(camera, size=size)

    cam_stream = camera.capture_continuous(image_storage, format="bgr", use_video_port=True)
    for raw_frame in cam_stream:
        frame = raw_frame.array

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Encode frame to JPEG format
        result, encoded_image = cv2.imencode('.jpg', frame, encode_param)
        frame_bytes = encoded_image.tostring()

        yield frame_bytes

        image_storage.truncate(0)


