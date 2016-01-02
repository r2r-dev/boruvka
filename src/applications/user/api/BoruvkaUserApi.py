from src.applications.base.api.BoruvkaBaseApi import (
    BoruvkaBaseApi,
    jsonize,
)
from src.applications.user.storage.BoruvkaUserStorage import BoruvkaUserStorage


class BoruvkaUserApi(BoruvkaBaseApi):
    def list_users(self):
        example_user = BoruvkaUserStorage()
        users = self._dao.list(example_user)
        return users
