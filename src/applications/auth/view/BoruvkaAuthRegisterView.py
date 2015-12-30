from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaAuthRegisterView(BoruvkaBaseView):
    __template = 'webroot/html/BoruvkaAuthRegisterTemplate.tmpl'

    def __init__(self, translation=None):
        BoruvkaBaseView.__init__(
            self,
            self.__template,
            translation,
        )

        self.register = "Register"
        self.login = "Login"
        self.username = "Username"
        self.password = "Password"
        self.password_confirm = "Confirm Password"
