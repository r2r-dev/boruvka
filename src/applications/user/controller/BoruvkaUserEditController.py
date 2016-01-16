from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.base.api.BoruvkaBaseApi import BoruvkaApiException
from src.applications.user.view.BoruvkaUserEditView import BoruvkaUserEditView
from src.applications.setting.query.BoruvkaSettingQuery import BoruvkaSettingQuery

from webob import Response


# Open database connection
class BoruvkaUserEditController(BoruvkaAuthorizedController):
    def get(self, user_id):
        api = BoruvkaUserApi(self.dao)

        user = api.get_user(
            id=user_id,
        )

        setting_query = BoruvkaSettingQuery(self.dao)
        user_settings = setting_query.get_user_settings(user_id)
        allowed_settings = setting_query.get_settings()
        translation = user_settings['language']

        view = BoruvkaUserEditView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._user = user
        view._settings = allowed_settings
        view._user_settings = user_settings

        response = Response()
        response.body = view.render()
        return response

    def post(self, user_id):
        api = BoruvkaUserApi(self.dao)
        params = self.request.params

        message = None
        error = None

        response_dict = {}
        for key, value in params.items():
            response_dict[key] = value

        try:
            api.update_user(
                user_id=user_id,
                payload=response_dict,
            )
        except BoruvkaApiException, e:
            error = e
        else:
            message = "Saved"

        user = api.get_user(
            id=user_id,
        )

        setting_query = BoruvkaSettingQuery(self.dao)
        user_settings = setting_query.get_user_settings(user_id)
        allowed_settings = setting_query.get_settings()
        translation = user_settings['language']

        view = BoruvkaUserEditView(
            translation=translation,
        )

        view._full = not self.request.is_xhr
        view._user = user
        view._settings = allowed_settings
        view._user_settings = user_settings

        view.message = message
        view.error = error

        response = Response()
        response.body = view.render()
        return response
