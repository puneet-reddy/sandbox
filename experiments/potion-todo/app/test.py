import unittest
import requests
import json
from app.main import todo_app
from app.config import api_config
from app.extensions import db
import json


class TestTodo(unittest.TestCase):
    
    def setUp(self):

        self.headers = {
            'Authorization': 'Basic YXBpdXNlcjAwMTphcGl1c2VyMDAx',
            'Content-Type': 'application/json'
        }

        self.data = {
            "name": "Make a Flask application",
            "active": 1
        }


    def test_post(self):

        app = todo_app(api_config['test'])
        client = app.test_client()
        with app.app_context():
            db.create_all()

        res = client.post("/todo", headers=self.headers, data=json.dumps(self.data))
        self.assertEqual(res.status_code, 200)


    def test_get_all(self):

        app = todo_app(api_config['test'])
        client = app.test_client()
        with app.app_context():
            db.create_all()

        res = client.get("/todo", headers=self.headers)
        self.assertEqual(res.status_code, 200)
    
    
    # def test_get_one(self):
    #     pass
    
    # def test_item_not_exist(self):
    #     pass
    
    
    # def test_update(self):
    #     pass
    
    # def test_update_error(self):
    #     pass
    
    # def test_delete(self):
    #     pass

    # def tearDown(self):
    #     with self.app.app_context():
    #         db.session.remove()
    #         db.drop_all()


if __name__ == "__main__":
    unittest.main()