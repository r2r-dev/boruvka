from src.applications.auth.application.BoruvkaAuthApplication import BoruvkaAuthApplication
from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.dispatcher.application.BoruvkaDispatcherApiApplication import BoruvkaDispatcherApiApplication
from src.applications.home.application.BoruvkaHomeApplication import BoruvkaHomeApplication
from src.applications.user.application.BoruvkaUserApplication import BoruvkaUserApplication
from src.utils.dao.BoruvkaSQLDao import BoruvkaSQLDao
from src.conf import settings


class BoruvkaDispatcherApplication(BoruvkaBaseApplication):
    def __init__(self, **config):
        BoruvkaBaseApplication.__init__(
            self,
            **config
        )

        dao = BoruvkaSQLDao(
            host=settings.db_host,
            username=settings.db_username,
            password=settings.db_password,
            database=settings.db_database,
            keepalive=False,
            autocommit=True,
        )

        self._dispatch_config = {
            'dao': dao,
        }

    def _set_routes(self):
        self.mapper.connect(
            '',
            '/',
            app=BoruvkaHomeApplication,
        )
        self.mapper.connect(
            'api',
            '/api{path_info:.*}',
            app=BoruvkaDispatcherApiApplication,
        )
        self.mapper.connect(
            'auth',
            '/auth{path_info:.*}',
            app=BoruvkaAuthApplication,
        )
        self.mapper.connect(
            'user',
            '/user{path_info:.*}',
            app=BoruvkaUserApplication,
        )

    def _get_route(self, **kwargs):
        match = kwargs['match']
        return match['app'](**self._dispatch_config)
