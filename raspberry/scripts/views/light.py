import flask
from view import View
import RPi.GPIO as GPIO


class LightViev(View):
    """Using GPIO pins via get-requests"""
    route = "/lights"
    GPIO.setmode(GPIO.BCM)

    def on_request(self, request):
        agrs = request.args
        try:
            pin = agrs['pin']
            state = agrs['state']
        except Exception:
            return flask.Response(405)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH if state == 1 else GPIO.LOW)
