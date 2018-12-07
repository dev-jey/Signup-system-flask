import json

from .base_test import TestsForApi


class TestSignup(TestsForApi):
    def test_successful_signup(self):
        '''Test for a successful signup'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Account created successfully")
        self.assertEqual(response.status_code, 201)
    
    def test_signup_missing_username(self):
        '''Test signup with no username given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        data=json.dumps({
                                            "username": "",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter a username")
        self.assertEqual(response.status_code, 401)
    
    def test_signup_missing_email(self):
        '''Test signup with no email given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter an email")
        self.assertEqual(response.status_code, 401)
    
    def test_signup_missing_password(self):
        '''Test signup with no password given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": ""
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter a password")
        self.assertEqual(response.status_code, 401)