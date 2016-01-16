from src.applications.base.api.BoruvkaBaseApi import (
    BoruvkaBaseApi,
    BoruvkaApiException,
    jsonize,
)
from src.applications.user.storage.BoruvkaUserStorage import BoruvkaUserStorage
from src.applications.user.query.BoruvkaUserQuery import BoruvkaUserQuery
from src.applications.setting.query.BoruvkaSettingQuery import BoruvkaSettingQuery
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi


class BoruvkaUserApi(BoruvkaBaseApi):
    def list_users(self):
        example_user = BoruvkaUserStorage()
        users = self._dao.list(example_user)
        return users

    def get_user(self, id):
        user_query = BoruvkaUserQuery(self._dao)
        user = user_query.get_user(
            id=id,
        )
        return user

    @jsonize
    def update_user(self, user_id, payload):
        user_query = BoruvkaUserQuery(self._dao)
        settings_query = BoruvkaSettingQuery(self._dao)

        user = user_query.get_user(
            id=user_id,
        )

        username = payload['username']
        if len(username) > 0:
            user.username = username
        else:
            raise BoruvkaApiException("Username cannot be empty")

        password = payload['password']
        if len(password) > 0:
            user.password = BoruvkaAuthApi.hash_password(
                username,
                password,
            )

        self._dao.update(user)

        # TODO, make setting options more generic
        options = {
            'language': payload['language'],
            'color': payload['color'],
        }

        settings_query.set_user_settings(
            user_id=user_id,
            options=options,
        )

        #image = payload['image']

        return
