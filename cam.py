from flask import Flask, Response, render_template
from picamera import PiCamera
from time import sleep

app = Flask(__name__)
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 30

def generate_frames():
    camera.start_preview()
    # Adjust camera settings as needed (resolution, framerate, etc.)
    camera.resolution = (640, 480)
    camera.framerate = 30
    sleep(2)  # Allow camera to warm up
    while True:
        # Capture frame from the camera
        camera.capture('temp.jpg')  # Capture to a temporary file
        with open('temp.jpg', 'rb') as f:
            frame = f.read()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

