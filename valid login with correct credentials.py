import requests
import unittest

class TestLogin(unittest.TestCase):
    def test_valid_login(self):
        url = "https://test.beeznests.com/new-login"
        payload = {
            "username": "madtuzzi@gmail.com",
            "password": "Hatter$1982"
        }
        response = requests.post(url, data=payload)
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on the expected behavior after a successful login

if __name__ == '__main__':
    unittest.main()
