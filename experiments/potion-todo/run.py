from app.main import todo_app
from app.config import api_config


if __name__ == '__main__':
    app = todo_app(api_config['dev'])
    app.run()
