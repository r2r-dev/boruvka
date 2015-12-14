from src.applications.base.application.BoruvkaBaseApplication import BoruvkaBaseApplication
from src.applications.dispatcher.application.BoruvkaDispatcherApiApplication import BoruvkaDispatcherApiApplication
from src.applications.hello.application.BoruvkaHelloApplication import BoruvkaHelloApplication
from src.applications.home.application.BoruvkaHomeApplication import BoruvkaHomeApplication
from src.applications.auth.application.BoruvkaAuthApplication import BoruvkaAuthApplication
from src.dao.BoruvkaSQLDao import BoruvkaSQLDao


class BoruvkaDispatcherApplication(BoruvkaBaseApplication):
    def __init__(self, **config):
        BoruvkaBaseApplication.__init__(
            self,
            **config
        )

        dao = BoruvkaSQLDao(
            host=self.config['database_host'],
            username=self.config['database_username'],
            password=self.config['database_password'],
            database=self.config['database'],
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
            'hello',
            '/hello{path_info:.*}',
            app=BoruvkaHelloApplication,
        )
        self.mapper.connect(
            'auth',
            '/auth{path_info:.*}',
            app=BoruvkaAuthApplication,
        )

    def _get_route(self, **kwargs):
        match = kwargs['match']
        return match['app'](**self._dispatch_config)
