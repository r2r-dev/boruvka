from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.auth.controller.BoruvkaAuthRegisterApiController import BoruvkaAuthRegisterApiController
from src.applications.auth.controller.BoruvkaAuthLoginApiController import BoruvkaAuthLoginApiController


class BoruvkaAuthApiApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'register',
            '/api/auth/register',
            controller=BoruvkaAuthRegisterApiController,
            conditions=dict(method=["POST"]),
            action='post',
        )
        self.mapper.connect(
            'login',
            '/api/auth/login',
            controller=BoruvkaAuthLoginApiController,
            conditions=dict(method=["POST"]),
            action='post',
        )
