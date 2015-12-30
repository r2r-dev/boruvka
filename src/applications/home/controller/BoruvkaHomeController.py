from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController
from src.applications.user.query.BoruvkaUserQuery import BoruvkaUserQuery

from src.applications.home.view.BoruvkaHomeView import BoruvkaHomeView
from webob import Response


# Open database connection
class BoruvkaHomeController(BoruvkaAuthorizedController):
    def get(self):
        translation = list(self.request.accept_language)[0]
        view = BoruvkaHomeView(translation)

        # TODO: move this to api
        user_id = self.session['user_id']
        user_query = BoruvkaUserQuery(self.dao)
        user = user_query.get_user(id=user_id)

        view.user = user.username

        response = Response()
        response.body = view.render()
        return response
