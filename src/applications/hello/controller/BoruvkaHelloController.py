from src.applications.auth.controller.BoruvkaAuthorizedController import BoruvkaAuthorizedController


# Open database connection
class BoruvkaHelloController(BoruvkaAuthorizedController):
    def get(self):
        return "GET from BoruvkaHelloController"

    def post(self):
        return "POST from BoruvkaHelloController"
