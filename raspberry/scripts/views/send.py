import flask
from view import View


class SendViev(View):
    """
    Here will be implemetation of sending bytes via I2C from web request
    """
    route = "/send"

    def on_request(self, request):
        args = request.args
        return args
