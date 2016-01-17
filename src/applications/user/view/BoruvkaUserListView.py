from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaUserListView(BoruvkaBaseView):
    __template = 'webroot/html/BoruvkaUserListTemplate.tmpl'

    def __init__(self, translation=None):
        BoruvkaBaseView.__init__(
            self,
            self.__template,
            translation,
        )

        self.title = "User List"
        self._users = {}
        self._users_settings = {}
