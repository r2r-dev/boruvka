from src.applications.base.controller.BoruvkaBaseController import BoruvkaBaseController
from src.applications.auth.api.BoruvkaAuthApi import BoruvkaAuthApi
from src.applications.auth.view.BoruvkaAuthLoginView import BoruvkaAuthLoginView
from webob import (
    Response,
    exc,
)


# Open database connection
class BoruvkaAuthLoginController(BoruvkaBaseController):
    def get(self):
        # TODO: move translations handling to BaseController
        translation = list(self.request.accept_language)[0]
        view = BoruvkaAuthLoginView(translation)
        response = Response()
        response.body = view.render()
        return response

    def post(self):
        params = self.request.params
        api = BoruvkaAuthApi(self.dao)
        request_dict = {}
        for key, value in params.items():
            request_dict[key] = value
        user_id, token_value = api.login(
            payload=request_dict,
        )

        if user_id:
            self.session['user_id'] = user_id
            response = exc.HTTPMovedPermanently(location=self.request.application_url)
            response.set_cookie(
                name='Token',
                value=token_value,
            )
            self.session.save()
            self.session.persist()
            return response
        else:
            # TODO: move translations handling to BaseController
            translation = list(self.request.accept_language)[0]
            view = BoruvkaAuthLoginView(translation)
            view.error = "Unauthorized"
            response = Response()
            response.body = view.render()
            #response = exc.HTTPUnauthorized()
        return response
