from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi


class BoruvkaAuthLogoutApiController(BoruvkaAuthorizedController):
    def get(self):
        authorization_header = self.request.authorization
        token_value = authorization_header[1]

        api = BoruvkaAuthApi(self.dao)
        api.invalidate_token(token_value)

        return 'Token invalidated!'
