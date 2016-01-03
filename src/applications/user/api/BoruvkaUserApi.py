from src.applications.base.api.BoruvkaBaseApi import (
    BoruvkaBaseApi,
    jsonize,
)
from src.applications.user.storage.BoruvkaUserStorage import BoruvkaUserStorage
from src.applications.user.query.BoruvkaUserQuery import BoruvkaUserQuery


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