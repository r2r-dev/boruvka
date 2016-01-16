from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.api.BoruvkaUserApi import BoruvkaUserApi
from src.applications.base.api.BoruvkaBaseApi import BoruvkaApiException
from src.applications.user.view.BoruvkaUserEditView import BoruvkaUserEditView
from src.applications.setting.query.BoruvkaSettingQuery import BoruvkaSettingQuery

from webob import Response


# Open database connection
class BoruvkaUserEditController(BoruvkaAuthorizedController):
    def get(self, user_id):
        user_api = BoruvkaUserApi(self.dao)

        viewer_id = self.session['user_id']

        user = user_api.get_user(id=user_id)

        setting_query = BoruvkaSettingQuery(self.dao)

        user_settings = setting_query.get_user_settings(user_id)
        allowed_settings = setting_query.get_settings()

        viewer_settings = setting_query.get_user_settings(viewer_id)
        translation = viewer_settings['language']
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
        user_api = BoruvkaUserApi(self.dao)
        viewer_id = self.session['user_id']
        params = self.request.params

        message = None
        error = None

        response_dict = {}
        for key, value in params.items():
            response_dict[key] = value

        try:
            user_api.update_user(
                user_id=user_id,
                payload=response_dict,
            )
        except BoruvkaApiException, e:
            error = e
        else:
            message = "Saved"

        user = user_api.get_user(
            id=user_id,
        )

        setting_query = BoruvkaSettingQuery(self.dao)
        user_settings = setting_query.get_user_settings(user_id)
        allowed_settings = setting_query.get_settings()

        viewer_settings = setting_query.get_user_settings(viewer_id)
        translation = viewer_settings['language']
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
