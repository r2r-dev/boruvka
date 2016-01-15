from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.user.view.BoruvkaUserEditView import BoruvkaUserEditView
from webob import Response


# Open database connection
class BoruvkaUserEditController(BoruvkaAuthorizedController):
    def get(self, user_id):
        api = BoruvkaUserApi(self.dao)

        user = api.get_user(
            id=user_id,
        )

        # TODO: move translations handling to BaseController
        translation = list(self.request.accept_language)[0]
        view = BoruvkaUserEditView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._user = user

        response = Response()
        response.body = view.render()
        return response
