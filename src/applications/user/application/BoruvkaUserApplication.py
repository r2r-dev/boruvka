from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.user.controller.BoruvkaUserListController import BoruvkaUserListController
from src.applications.user.controller.BoruvkaUserShowController import BoruvkaUserShowController
from src.applications.user.controller.BoruvkaUserEditController import BoruvkaUserEditController


class BoruvkaUserApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'user',
            '/user/',
            controller=BoruvkaUserListController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{user_id}',
            controller=BoruvkaUserShowController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{user_id}/edit',
            controller=BoruvkaUserEditController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/user/{user_id}/edit',
            controller=BoruvkaUserEditController,
            conditions=dict(method=["POST"]),
            action='post',
        )
        '''
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