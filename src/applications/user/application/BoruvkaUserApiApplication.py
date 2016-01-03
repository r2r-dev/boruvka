from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.user.controller.BoruvkaUserListApiController import BoruvkaUserListApiController


class BoruvkaUserApiApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'user',
            '/api/user/',
            controller=BoruvkaUserListApiController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        '''
        self.mapper.connect(
            'user',
            '/api/user/{id}',
            controller=BoruvkaUserShowApiController,
            conditions=dict(method=["GET"]),
            action='get',
        )
        self.mapper.connect(
            'user',
            '/api/user/{id}/edit',
            controller=BoruvkaUserEditApiController,
            conditions=dict(method=["POST"]),
            action='post',
        )
        self.mapper.connect(
            'user',
            '/api/user/{id}/delete',
            controller=BoruvkaUserDeleteApiController,
            conditions=dict(method=["DELETE"]),
            action='delete',
        )
        '''
