import flask
from view import View
from asset import AssetManager


class FaviconView(View):
    """
    Favicon view.

    Sometimes browsers (i.e Chrome, Safari) request not only favicon.ico
    but also some its variations, like "apple-touch-icon.png" (requested
    by Safari sometimes). To optimize browsers work, its better to store
    not only just "favicon.ico" (which would still be fine), but also some
    other icons.
    """

    routes = [
        "/favicon.ico",
        "/favicon-16x16.png",
        "/apple-touch-icon.png",
        "/android-chrome-192x192.png",
        "/android-chrome-512x512.png",
        "/favicon-32x32.png"]

    def on_request(self, _, route):
        icon_name = route[1:]
        return flask.send_file(AssetManager.get_icon(icon_name))
