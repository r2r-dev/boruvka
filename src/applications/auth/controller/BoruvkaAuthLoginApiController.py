from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi


# Open database connection
class BoruvkaAuthLoginApiController(BoruvkaBaseController):
    def post(self):

        api = BoruvkaAuthApi(self.dao)
        response = api.login(
            payload=self.request.text,
        )

        return response
