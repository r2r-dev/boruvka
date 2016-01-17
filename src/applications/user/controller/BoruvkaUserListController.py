from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.setting.query.BoruvkaSettingQuery import BoruvkaSettingQuery
from src.applications.user.view.BoruvkaUserListView import BoruvkaUserListView
from webob import Response


# Open database connection
class BoruvkaUserListController(BoruvkaAuthorizedController):
    def get(self):
        api = BoruvkaUserApi(self.dao)
        users = api.list_users()

        setting_query = BoruvkaSettingQuery(self.dao)
        users_settings = {}
        for user in users:
            users_settings[user.id] = setting_query.get_user_settings(user.id)


        # TODO: move translations handling to BaseController
        translation = list(self.request.accept_language)[0]
        view = BoruvkaUserListView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._users = users
        view._users_settings = users_settings

        response = Response()
        response.body = view.render()
        return response
