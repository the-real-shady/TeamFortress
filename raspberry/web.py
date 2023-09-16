from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import threading
GPIO.setmode(GPIO.BCM)


def light(port) -> None:
    GPIO.output(port, GPIO.HIGH)
    GPIO.output(port, GPIO.LOW)
    GPIO.cleanup(port)



app = Flask(__name__)


commands = {'lights': 0}


@app.route('/set_lights', methods=['GET'])
def add_command():
    number = int(request.args.get('state'))
    GPIO.setup(number, GPIO.OUT)
    GPIO.output(number, GPIO.HIGH)
    threading.Timer(30, light, args=[number])
    return 
    


@app.route('/get_lights', methods=['GET'])
def get_commands():
    return jsonify({"commands": commands['lights']})


if __name__ == '__main__':
    app.run(debug=True)
