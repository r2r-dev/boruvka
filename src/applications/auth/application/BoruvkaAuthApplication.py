from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.auth.controller.BoruvkaAuthLoginController import BoruvkaAuthLoginController
from src.applications.auth.controller.BoruvkaAuthRegisterController import BoruvkaAuthRegisterController


class BoruvkaAuthApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'auth',
            '/auth/login',
            controller=BoruvkaAuthLoginController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'auth',
            '/auth/login',
            controller=BoruvkaAuthLoginController,
            conditions=dict(method=["POST"]),
            action='post',
        )
        self.mapper.connect(
            'auth',
            '/auth/register',
            controller=BoruvkaAuthRegisterController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'auth',
            '/auth/register',
            controller=BoruvkaAuthRegisterController,
            conditions=dict(method=["POST"]),
            action='post',
        )
