from src.applications.base.view.BoruvkaBaseView import BoruvkaBaseView


class BoruvkaHomeView(BoruvkaBaseView):
    __template = 'webroot/html/BoruvkaHomeTemplate.tmpl'

    def __init__(self, translation=None):
        BoruvkaBaseView.__init__(
            self,
            self.__template,
            translation,
        )

        self.title = "Home Page"
        self.tasks = "Tasks"
        self.machines = "Machines"
        self.users = "Users"
        self.settings = "Settings"
        self.profile = "Profile"
        self.logout = "Logout"

        self.user = None