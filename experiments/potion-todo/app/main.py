
"""
Todo Restful App made using flask-potion
"""

from flask import Flask
from flask_potion import Api
from flask_login import login_required
from flask_potion.contrib.principals import principals
from flask_potion.contrib.alchemy import SQLAlchemyManager


from app.extensions import db
from app.extensions import principal
from app.extensions import login_manager
from app.extensions import cors

from app.resources.todo import TodoResource
from app.models.apiuser import ApiUser




def todo_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)

    db.app = app
    db.init_app(app)

    login_manager.init_app(app)
    principal.init_app(app)
    cors.init_app(app)

    api = Api(app, decorators=[login_required], default_manager=principals(SQLAlchemyManager))
    api.add_resource(TodoResource)
    

    
    with app.app_context():
        from app import auth
        #db.drop_all()
        db.create_all()
        db.session.add(ApiUser(username="apiuser001", is_admin=True))
        db.session.commit()
        
    return app


