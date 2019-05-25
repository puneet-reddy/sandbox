from flask import current_app

from flask_principal import Identity
from flask_principal import UserNeed
from flask_principal import AnonymousIdentity
from flask_principal import identity_loaded
from flask_principal import RoleNeed
from flask_login import current_user

from app.extensions import login_manager
from app.extensions import principal
from app.models.apiuser import ApiUser



@login_manager.request_loader
def load_user_from_request(request):
    if request.authorization:
        username, password = request.authorization.username, request.authorization.password
        
        if username == password:
            return ApiUser.query.filter_by(username=username).first()
    return None



@principal.identity_loader
def read_identity_from_flask_login():
    if current_user.is_authenticated:
        return Identity(current_user.id)
    return AnonymousIdentity()


@identity_loaded.connect_via(current_app)
def on_identity_loaded(sender, identity):

    if not isinstance(identity, AnonymousIdentity):
        identity.provides.add(UserNeed(identity.id))

        if current_user.is_editor:
            identity.provides.add(RoleNeed('editor'))

        if current_user.is_admin:
            identity.provides.add(RoleNeed('admin'))
