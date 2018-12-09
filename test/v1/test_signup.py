import json

from .base_test import TestsForApi


class TestSignup(TestsForApi):
    def test_successful_signup(self):
        '''Test for a successful signup'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.coms",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Account created successfully")
        self.assertEqual(response.status_code, 201)
    
    def test_signup_missing_username(self):
        '''Test signup with no username given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter a username")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_missing_email(self):
        '''Test signup with no email given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter an email")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_missing_password(self):
        '''Test signup with no password given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": ""
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter a password")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_missing_username_key(self):
        '''Test signup with no username key given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "": "jey21",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Username is a required field")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_missing_email_key(self):
        '''Test signup with no email key given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Email is a required field")
        self.assertEqual(response.status_code, 400)

    def test_signup_missing_password_key(self):
        '''Test signup with no password key given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Password is a required field")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_existing_username(self):
        '''Test signup for an already existing username'''
        self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james2@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Username already taken")
        self.assertEqual(response.status_code, 406)
    
    def test_signup_existing_email(self):
        '''Test signup for an already existing email'''
        self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey212",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey214",
                                            "email": "james@gmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Email already taken")
        self.assertEqual(response.status_code, 406)
    
    def test_signup_with_wrong_email(self):
        '''Test signup with an invalid email given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "jamesgmail.com",
                                            "password": "James@12"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Enter a valid email")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_with_a_short_password(self):
        '''Test signup with a password less than 6 characters given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": "Jam"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Password must be long than 6 characters")
        self.assertEqual(response.status_code, 400)
    
    def test_signup_with_a_many_fields_given(self):
        '''Test signup with more than enough fields given'''
        response = self.test_client.post("/api/v1/auth/signup",
                                        headers = self.header,
                                        data=json.dumps({
                                            "username": "jey21",
                                            "email": "james@gmail.com",
                                            "password": "Jam",
                                            "address":"Nairobi"
                                        })
                                        )
        feedback = json.loads(response.data)
        self.assertEqual(feedback["message"], "Only 3 fields are required")
        self.assertEqual(response.status_code, 400)
    
    