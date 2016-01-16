from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.home.view.BoruvkaHomeView import BoruvkaHomeView
from webob import Response


# Open database connection
class BoruvkaHomeController(BoruvkaAuthorizedController):
    def get(self):
        translation = list(self.request.accept_language)[0]
        view = BoruvkaHomeView(translation)

        # TODO: move this to api
        user_id = self.session['user_id']
        user_api = BoruvkaUserApi(self.dao)
        user = user_api.get_user(id=user_id)

        view.user = user

        response = Response()
        response.body = view.render()
        return response
