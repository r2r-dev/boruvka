from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.view.BoruvkaAuthRegisterView import BoruvkaAuthRegisterView
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi
from webob import (
    exc,
    Response,
)


class BoruvkaAuthRegisterController(BoruvkaBaseController):
    def get(self):
        translation = list(self.request.accept_language)[0]
        view = BoruvkaAuthRegisterView(translation)
        response = Response()
        response.body = view.render()
        return response

    def post(self):
        # TODO: check whether passwords match
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
