from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.user.view.BoruvkaUserListView import BoruvkaUserListView
from webob import Response


# Open database connection
class BoruvkaUserListController(BoruvkaAuthorizedController):
    def get(self):
        api = BoruvkaUserApi(self.dao)
        users = api.list_users()

        # TODO: move translations handling to BaseController
        translation = list(self.request.accept_language)[0]
        view = BoruvkaUserListView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._users = users

        response = Response()
        response.body = view.render()
        return response
