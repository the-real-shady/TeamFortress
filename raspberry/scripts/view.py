from __future__ import annotations
from flask import Request, request as g_request, views, typing


class View(views.View):
    """
    View represents single or multiple webpage (s). For example, SetLightsView
    can represent single "/set_lights" page. Every view gets registered before
    the server runs. It gets registered automatically (so there is no need to
    call app.route(...) or whatever).

    Every class that derives View must declare either "route" variable which indicates
    its address (i.e indicates its url) or "routes" variable which specifies the list
    of urls for which is view is responsible. When using "routes" variable, "on_request"
    function should additionally accept "route" argument, which will contain a string -
    - name of the route.

    For example, SetLightsView should define "route" variable as follows: route = "/set_lights"
    and FaviconView can define "routes" variable as follows: routes = ["/favicon.ico",
    "apple-touch-icon.png"].

    Derived classes are also allowed to declare some flask- related stuff such as "methods",
    "decorators", "provide_automatic_options" ... etc.
    """

    def __init__(self, route: str | None = None) -> None:
        """
        Initialize the view.

        Parameters
        ----------
        route : str | None
            Route for this view if it support multiple routes, otherwise None.
        """
        super().__init__()
        self.route = route

    def dispatch_request(self, *args, **kwargs) -> typing.ResponseReturnValue:
        if self.route:
            kwargs["route"] = self.route
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
        flask.ResponseReturnValue
            Any object convertible to response
        """
        raise NotImplementedError()

    @staticmethod
    def enumerate_children() -> list[View]:
        return View.__subclasses__()
