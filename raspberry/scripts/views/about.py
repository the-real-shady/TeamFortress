import flask
from asset import AssetManager
from view import View


class AboutView(View):
    route = "/about"

    def on_request(self, _):
        index = AssetManager.get_html("about/index.html")
        return flask.send_file(index)
