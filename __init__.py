from src.applications.dispatcher.application.BoruvkaDispatcherApplication import BoruvkaDispatcherApplication

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
application = BoruvkaDispatcherApplication(**config)
