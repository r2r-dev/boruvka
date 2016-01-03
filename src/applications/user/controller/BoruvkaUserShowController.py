from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.user.view.BoruvkaUserShowView import BoruvkaUserShowView
from webob import Response


# Open database connection
class BoruvkaUserShowController(BoruvkaAuthorizedController):
    def get(self, user_id):
        api = BoruvkaUserApi(self.dao)

        user = api.get_user(
            id=user_id,
        )

        # TODO: move translations handling to BaseController
        translation = list(self.request.accept_language)[0]
        view = BoruvkaUserShowView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._user = user

        response = Response()
        response.body = view.render()
        return response
