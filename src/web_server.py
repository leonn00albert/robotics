from flask import Flask, render_template, request

app = Flask(__name__)


# This variable will store the current robot command
robot_command = ""

@app.route('/')
def index():
    return render_template('index.html', command=robot_command)

@app.route('/forward')
def forward():
    global robot_command
    distance = int(request.args.get('distance', 100))  # Default to 100 if not provided
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    distance_in_ticks = EncoderCounter.mm_to_ticks(distance)
    bot.drive.distances(distance_in_ticks, distance_in_ticks)
    bot.motor.stop()
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
    # Add code to send right command to the robot
    return "Right command sent"

@app.route('/backward')
def backward():
    global robot_command
    speed = int(request.args.get('speed', 60))  # Default to 60 if not provided

    bot.motor.stop()
    # Add code to send backward command to the robot
    return "Backward command sent"

if __name__ == '__main__':
    app.run(host='robot.local', port=5000, debug=True)
