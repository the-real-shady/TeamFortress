import flask
from view import View


class IndexViev(View):
    route = "/"

    def on_request(self, request):
        return flask.render_template('index.html')
