from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi
from webob import (
    exc,
    Response,
)


class BoruvkaAuthRegisterController(BoruvkaBaseController):
    def get(self):
        # TODO: plug in templating system
        view_path = 'webroot/html/register.html'
        response = Response()
        response.body = open(view_path, 'rb').read()
        return response

    def post(self):
        params = self.request.params
        api = BoruvkaAuthApi(self.dao)
        response_dict = {}
        for key, value in params.items():
            response_dict[key] = value
        api_response = api.register(
            payload=response_dict,
        )

        if api_response:
            response = exc.HTTPMovedPermanently(location='/auth/login')
            return response
        else:
            response = exc.HTTPUnauthorized()
        return response
