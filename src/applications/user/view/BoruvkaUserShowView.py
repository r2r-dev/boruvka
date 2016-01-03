from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaUserShowView(BoruvkaBaseView):
    __template = 'webroot/html/BoruvkaUserShowTemplate.tmpl'

    def __init__(self, translation=None):
        BoruvkaBaseView.__init__(
            self,
            self.__template,
            translation,
        )

        self.title = "User"
        self.username = "Username"
        self.id = "Id"
        self.close = "Close"
        self._user = None
