from flask_potion import ModelResource
from app.models.todo import Todo
from flask_potion.routes import Route
from flask_potion import fields
from flask_potion.signals import before_create


class TodoResource(ModelResource):
    
    class Meta:
        model = Todo
        permissions = {
            'create': 'anybody',
            'update': 'is_admin'
        }
    
    class Schema:
        name = fields.String(description="Name of todo", min_length=2, max_length=120)
        active = fields.Integer(description="Todo status")
    



@before_create.connect_via(TodoResource)
def on_before_create_todo(sender, item):
    print(sender)
    print(item)
    