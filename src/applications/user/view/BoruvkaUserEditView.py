from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaUserEditView(BoruvkaBaseView):
    __template = 'webroot/html/BoruvkaUserEditTemplate.tmpl'

    def __init__(self, translation=None):
        BoruvkaBaseView.__init__(
            self,
            self.__template,
            translation,
        )

        self.title = "User"
        self.username = "Username"
        self.password = "Password"
        self.language = "Language"
        self.color = "Color"
        self.close = "Close"
        self.save = "Save"
        self._user = None
