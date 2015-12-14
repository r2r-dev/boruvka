from src.applications.dispatcher.application.BoruvkaDispatcherApplication import BoruvkaDispatcherApplication
from beaker.middleware import SessionMiddleware

'''
Note: technically we could use multiple WSGI servers for each app.
'''

# TODO: bootstrapping
config = {
  "admin_user": "admin",
  "admin_password": "password",
  "database_host": "localhost",
  "database_port": 3306,
  "database_username": "root",
  "database_password": "reverse",
  "database": "boruvka",
}

# Configure the SessionMiddleware
session_opts = {
    'session.type': 'file',
    'session.cookie_expires': True,
    'session.lockdir': 'sessionslock',
    'session.data_dir': 'sessionsdata',
    'auto': 'true',
}
boruvka = BoruvkaDispatcherApplication(**config)
application = SessionMiddleware(boruvka, session_opts)
