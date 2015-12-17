from src.applications.dispatcher.application.BoruvkaDispatcherApplication import BoruvkaDispatcherApplication
from beaker.middleware import SessionMiddleware

'''
Note: technically we could use multiple WSGI servers for each app.
'''

# Configure the SessionMiddleware
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.lockdir': 'sessionslock',
    'session.data_dir': 'sessionsdata',
    'auto': 'true',
}
boruvka = BoruvkaDispatcherApplication()
application = SessionMiddleware(boruvka, session_opts)
