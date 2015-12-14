from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from webob import Response


# Open database connection
class BoruvkaHomeController(BoruvkaAuthorizedController):
    def get(self):
        # TODO: plug in templating system
        view_path = 'webroot/html/index.html'
        response = Response()
        response.body = open(view_path, 'rb').read()
        return response
