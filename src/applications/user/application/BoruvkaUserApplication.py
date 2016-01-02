from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.user.controller.BoruvkaUserListController import BoruvkaUserListController


class BoruvkaUserApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'user',
            '/user/',
            controller=BoruvkaUserListController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        '''self.mapper.connect(
            'user',
            '/user/{id}',
            controller=BoruvkaUserShowController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{id}/edit',
            controller=BoruvkaUserEditController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{id}/edit',
            controller=BoruvkaUserEditController,
            conditions=dict(method=["POST"]),
            action='post',
        )
        self.mapper.connect(
            'user',
            '/user/{id}/delete',
            controller=BoruvkaUserDeleteController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{id}/delete',
            controller=BoruvkaUserDeleteController,
            conditions=dict(method=["POST"]),
            action='post',
        )
'''