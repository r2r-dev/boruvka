from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.hello.controller.BoruvkaHelloController import BoruvkaHelloController


class BoruvkaHelloApiApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'api/hello',
            '/api/hello',
            controller=BoruvkaHelloController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'api/hello',
            '/api/hello',
            controller=BoruvkaHelloController,
            conditions=dict(method=["POST"]),
            action='post',
        )
