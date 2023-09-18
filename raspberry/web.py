from flask import Flask, request, jsonify, send_file
import RPi.GPIO as GPIO
import threading
GPIO.setmode(GPIO.BCM)
ACTIVE_PORTS = set()
filename = 'pic.gif'


def light(port) -> None:
    GPIO.output(port, GPIO.LOW)
    GPIO.cleanup(port)
    ACTIVE_PORTS.remove(port)


app = Flask(__name__)


commands = {'lights': 0}


@app.route('/set_lights', methods=['GET'])
def add_command():
    number = int(request.args.get('port'))
    pwm = request.args.get('pwm', default=None)
    pwm = int(pwm) if pwm != None else None
    if pwm != None:
        pw = GPIO.PWM(number, 1000)
        pw.start(pwm)
    else:
        GPIO.setup(number, GPIO.OUT)
        GPIO.output(number, GPIO.HIGH)
    t = threading.Timer(30, light, args=[number])
    t.start()
    ACTIVE_PORTS.add(number)
    return jsonify({'Active ports': list(ACTIVE_PORTS)})


@app.route('/get_lights', methods=['GET'])
def get_commands():
    return jsonify({"commands": commands['lights']})


@app.route("/get_my_ip", methods=["GET"])
def get_my_ip():
    if request.remote_addr == '192.168.233.163':
        return send_file(filename, mimetype='image/gif')
    else:
        return jsonify({'ip': request.remote_addr}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')