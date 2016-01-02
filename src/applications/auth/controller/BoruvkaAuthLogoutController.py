from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi
from webob import exc


class BoruvkaAuthLogoutController(BoruvkaAuthorizedController):
    def get(self):
        response = exc.HTTPMovedPermanently(location="/")
        api = BoruvkaAuthApi(self.dao)

        token_value = self.request.cookies['Token']
        api.invalidate_token(token_value)
        response.delete_cookie('Token')
        self.session.delete()
        return response
