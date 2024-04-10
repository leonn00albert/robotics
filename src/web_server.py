from flask import Flask, render_template,Response, request
import time
import pi_camera_stream
from Robot import Robot, EncoderCounter


app = Flask(__name__)





bot = Robot()

# This variable will store the current robot command
robot_command = ""


@app.route('/')
def index():
    return render_template('index.html', command=robot_command)


def frame_generator():
    """This is our main video feed"""
    camera = pi_camera_stream.setup_camera()

    # allow the camera to warmup
    time.sleep(0.1)

    for frame in pi_camera_stream.start_stream(camera):
        encoded_bytes = pi_camera_stream.get_encoded_bytes_for_frame(frame)
        # Need to turn this into http multipart data.
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')
@app.route('/display')
def display():
    return Response(frame_generator(),
        mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/forward')
def forward():
    global robot_command
    distance = int(request.args.get('distance', 100))  # Default to 100 if not provided
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    distance_in_ticks = EncoderCounter.mm_to_ticks(distance)
    bot.drive.distances(distance_in_ticks, distance_in_ticks)
    bot.motor.stop()
    robot_command = f"Forward with distance {distance} and speed {speed}"
    # Add code to send forward command to the robot
    return "Forward command sent"

@app.route('/left')
def left():
    global robot_command
    distance = int(request.args.get('distance', 100))  # Default to 100 if not provided
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    distance_in_ticks = EncoderCounter.mm_to_ticks(distance)
    bot.drive.distances(0, distance_in_ticks)
    bot.motor.stop()
    robot_command = f"Left with distance {distance} and speed {speed}"
    # Add code to send left command to the robot
    return "Left command sent"

@app.route('/right')
def right():
    global robot_command
    distance = int(request.args.get('distance', 100))  # Default to 100 if not provided
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    distance_in_ticks = EncoderCounter.mm_to_ticks(distance)
    bot.drive.distances(distance_in_ticks, 0)
    bot.motor.stop()
    robot_command = f"Right with distance {distance} and speed {speed}"
    # Add code to send right command to the robot
    return "Right command sent"

@app.route('/backward')
def backward():
    global robot_command
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    bot.motor.stop()
    robot_command = f"Backward with speed {speed}"
    # Add code to send backward command to the robot
    return "Backward command sent"


if __name__ == '__main__':
    app.run(host='nodebot.local', port=5000, debug=True)
