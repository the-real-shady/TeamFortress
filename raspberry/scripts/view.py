from __future__ import annotations
from flask import Request, request as g_request, views, typing


class View(views.View):
    """
    View represents a single "webpage". For example, SetLightsView can
    represent single "/set_lights" page. Every view gets registered
    automatically (so there is no need to call app.route(...) or whatever).

    Every class that derives View must declare "route" variable which indicates
    its address (i.e indicates its url). For example, SetLightsView should define
    "route" variable as follows: route = "/set_lights". Derived classes are also
    allowed to declare some flask- related stuff such as "methods", "decorators",
    "provide_automatic_options" ... etc.
    """

    def __init__(self) -> None:
        super().__init__()

    def dispatch_request(self, *args, **kwargs) -> typing.ResponseReturnValue:
        try:
            return self.on_request(g_request, *args, **kwargs)
        except Exception as e:
            return str(e)

    def on_request(self, request: Request, *args, **kwargs) -> typing.ResponseReturnValue:
        """
        Handle request. Derived classes have to override this function.

        Parameters
        ----------
        request : Request
            Reference to the request

        args : Any
            Arguments referenced in the url rule (flask)

        kwargs : Any
            Arguments referenced in the url rule (flask)

        Returns
        -------
        flask.Response
            Response object
        """
        raise NotImplementedError()

    @staticmethod
    def enumerate_children() -> list[View]:
        return View.__subclasses__()
