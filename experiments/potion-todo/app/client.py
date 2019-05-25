from potion_client import Client
from requests.auth import AuthBase
from potion_client.exceptions import ItemNotFound


class HttpBasicAuth(AuthBase):
    """Attaches HTTP Basic Authentication to the given Request object."""
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Basic {}'.format(self.token)
        return r



client = Client('http://localhost:5000', auth=HttpBasicAuth("YXBpdXNlcjAwMTphcGl1c2VyMDAx"))

#client.User("apiuser001")

todo = client.Todo()

#todo.create(name="Develop an Flask Api", active=1)

todos = todo.instances()

for todo in todos:
    print("Todo :: {0} - {1}, Status: {2}".format(todo.id, todo.name, todo.active))


#get = todo.fetch(id=2)






