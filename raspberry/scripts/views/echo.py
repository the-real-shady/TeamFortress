from view import View


class EchoView(View):
    route = "/echo"

    def on_request(self, request):
        return request.get_data()
