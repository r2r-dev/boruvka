Boruvka - simple orchestration system based on WebOb

setup:
nginx (use supplied conf)
gunicorn --timeout 1000000 -b 127.0.0.1:8000 __init__:application
