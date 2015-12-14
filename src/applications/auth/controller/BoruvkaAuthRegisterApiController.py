from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi


# Open database connection
class BoruvkaAuthRegisterApiController(BoruvkaBaseController):
    def post(self):

        api = BoruvkaAuthApi(self.dao)
        response = api.register(
            payload=self.request.text,
        )

        return 'Response: {0:d}!'.format(response)
