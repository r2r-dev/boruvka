from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi
from webob import (
    Response,
    exc,
)


# Open database connection
class BoruvkaAuthLoginController(BoruvkaBaseController):
    def get(self):
        # TODO: plug in templating system
        view_path = 'webroot/html/login.html'
        response = Response()
        response.body = open(view_path, 'rb').read()
        return response

    def post(self):
        params = self.request.params
        api = BoruvkaAuthApi(self.dao)
        request_dict = {}
        for key, value in params.items():
            request_dict[key] = value
        api_response = api.login(
            payload=request_dict,
        )

        if api_response:
            response = exc.HTTPMovedPermanently(location=self.request.application_url)
            response.set_cookie(
                name='Token',
                value=api_response,
            )
            return response
        else:
            response = exc.HTTPUnauthorized()
        return response
