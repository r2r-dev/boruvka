from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi


# Open database connection
class BoruvkaAuthLoginApiController(BoruvkaBaseController):
    def post(self):

        api = BoruvkaAuthApi(self.dao)
        user_id, token_value = api.login(
            payload=self.request.text,
        )

        return token_value
