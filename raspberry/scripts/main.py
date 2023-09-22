import flask
from view import View
import importlib.util
from asset import AssetManager
import sys
import os


class RaspberryServer(flask.Flask):
    @staticmethod
    def find_views() -> list[tuple[str, str]]:
        """
        Find views.

        Returns
        -------
        list[tuple[str, str]]
            List of pairs where the first argument is the module name
            and second is the path to the module
        """
        VIEWS_FOLDER_NAME = "views"
        views_folder = os.path.join(os.path.dirname(__file__), VIEWS_FOLDER_NAME)
        views_files = list(filter(lambda x: os.path.splitext(x)[1] == ".py", os.listdir(views_folder)))

        views_names = map(lambda x: x[:-3], views_files)
        views_pathes = map(lambda x: os.path.join(views_folder, x), views_files)
        return list(zip(views_names, views_pathes))

    def __init__(self, addr: str, port: int):
        """Initialize server and load views from view/ subfolder"""
        super().__init__(__name__)

        self.addr = addr
        self.port = port

        for name, path in RaspberryServer.find_views():
            spec = importlib.util.spec_from_file_location(name, path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[name] = module
            spec.loader.exec_module(module)

        for view in View.enumerate_children():
            self._create_url_view(view)

    def _create_url_view(self, view: type[View]) -> None:
        if hasattr(view, "route"):
            self.add_url_rule(view.route, view_func=view.as_view(view.__name__))
            return

        if hasattr(view, "routes"):
            for route in view.routes:
                name = f"{view.__name__}_{route[1:]}"
                self.add_url_rule(route, view_func=view.as_view(name, route=route))
            return

        raise NotImplementedError(f"View {view.__class__} does not contain \"route\" field")

    def run_debug(self) -> None:
        return self.run(self.addr, self.port, True)

    def run_release(self) -> None:
        return self.run(self.addr, self.port, False)


def main() -> int:
    AssetManager.init()

    ip_address = "0.0.0.0"

    ENV_IP_NAME = "RASPBERRY_SERVER_IP"
    if ENV_IP_NAME in os.environ:
        ip_address = os.environ[ENV_IP_NAME]

    server = RaspberryServer(ip_address, 8080)
    server.run_debug()
    return 0


if __name__ == '__main__':
    sys.exit(main())
