import flask
from view import View


class SetLightsView(View):
    route = "/set_lights"

    def on_request(self, request):
        return flask.Response(status=501)
