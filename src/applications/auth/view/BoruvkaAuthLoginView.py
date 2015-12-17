from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaAuthLoginView(BoruvkaBaseView):
    def __init__(self, template, translation=None):
        BoruvkaBaseView.__init__(
            self,
            template,
            translation,
        )

        self.login = "Login"
        self.username = "Username"
        self.password = "Password"
