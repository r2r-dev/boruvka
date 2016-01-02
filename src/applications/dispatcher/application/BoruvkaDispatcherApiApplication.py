from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.auth.application.BoruvkaAuthApiApplication import BoruvkaAuthApiApplication
from src.applications.user.application.BoruvkaUserApiApplication import BoruvkaUserApiApplication


class BoruvkaDispatcherApiApplication(BoruvkaBaseApplication):
    def _set_routes(self):
        self.mapper.connect(
            'auth',
            '/api/auth{path_info:.*}',
            app=BoruvkaAuthApiApplication,
        )
        self.mapper.connect(
            'user',
            '/api/user{path_info:.*}',
            app=BoruvkaUserApiApplication,
        )

    def _get_route(self, **kwargs):
        match = kwargs['match']
        return match['app'](**self.config)
