'''Archivo que ejecuta la aplicacion'''

from config.config import server_config
from config.config import get_app
from config.config import run_app
from routes.history import create_routes_history

app = get_app(__name__)

server_config(app)
create_routes_history(app)

if __name__ == '__main__':
    run_app(app)
