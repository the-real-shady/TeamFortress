import flask
from view import View


class SendViev(View):
    """Implemetation of sending bytes via I2C from web request"""
    route = "/send"

    def on_request(self, request):
        return request.args
