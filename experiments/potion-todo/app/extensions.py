from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_principal import Principal
from flask_cors import CORS


db = SQLAlchemy()
login_manager = LoginManager()
principal = Principal()
cors = CORS(resources={r"*": {"origins": "*"}})

