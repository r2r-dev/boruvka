from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.home.controller.BoruvkaHomeController import BoruvkaHomeController


class BoruvkaHomeApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            '',
            '/',
            controller=BoruvkaHomeController,
            conditions=dict(method=["GET"]),
            action='get',
        )
