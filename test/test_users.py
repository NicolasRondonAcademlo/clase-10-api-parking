from telnetlib import SE
from wsgiref import headers
from core.models import User
from rest_framework.test import APITestCase
import pprint

class TestCrudUser(APITestCase):
    def setUp(self) -> None:
        result =self.client.post('/api/users/',
        {
            "email": "prueba5888@gmail.com",
            "password": "688a7dada",
            "first_name": "prueba",
            "last_name": "prueba"
        }
        )
        self.token = self.client.post('/api/token/', {
            "email": "prueba5888@gmail.com",
            "password": "688a7dada"}
            )
    
    def test_create_user(self):
        result =self.client.post('/api/users/',
        {
            "email": "prueba58@gmail.com",
            "password": "688a7dada",
            "first_name": "prueba",
            "last_name": "prueba"
        }
        )
        assert  result.json()["id"] == 2
        assert result.status_code == 201

    def test_edit_user(self):
        token = self.token.json()["access"]
        result =self.client.patch(path='/api/users/1/',
        data={"first_name": "prueba editada"},
        HTTP_AUTHORIZATION = "Bearer " + token)

     
        assert result.json()["first_name"] == "prueba editada"

    def test_read_user(self):
        token = self.token.json()["access"]
        result =self.client.get(path='/api/users/1/',HTTP_AUTHORIZATION = "Bearer " + token)
        assert result.status_code == 200

    def test_delete_user(self): #unitest
        token = self.token.json()["access"]
        result =self.client.delete(path='/api/users/1/',HTTP_AUTHORIZATION = "Bearer " + token)
        assert result.status_code ==204
        