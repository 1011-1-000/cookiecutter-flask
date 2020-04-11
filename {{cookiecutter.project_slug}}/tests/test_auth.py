import json

from app.common.errors import (InvalidTokenError,
                               NotMatchOrUserDoesNotExistsError,
                               TokenBlackListedError, TokenMissedError)
from tests.test_basics import BasicsTestCase
from tests.utils.common import login, register
from tests.utils.rest import RestMixin


class TestAuthBlueprint(BasicsTestCase):

    def test_login(self):
        response = register(self.client)
        self.assertEqual(response.status_code, 201)

        login_response = login(self.client)
        data = json.loads(login_response.data.decode())
        self.assertTrue(data.get('Authorization'))
        self.assertEqual(login_response.status_code, 200)

    def test_login_with_wrong_password(self):
        register(self.client)

        with self.client:
            user_data = json.dumps(dict(
                email='example@gmail.com',
                password='1234567',
            ))
            login_response = RestMixin.post(
                self.client, '/auth/login', user_data)

        self.assertEqual(login_response.status_code, 400)
        self.assertRaises(NotMatchOrUserDoesNotExistsError)

    def test_logout_and_block_token(self):
        register(self.client)
        login_response = login(self.client)
        headers = dict(
            Authorization='Bearer ' + json.loads(
                login_response.data.decode()
            )['Authorization']
        )
        logout_response = RestMixin.get(
            self.client, '/auth/logout', headers=headers)
        self.assertEqual(logout_response.status_code, 200)
        login_response = login(self.client)
        self.assertRaises(TokenBlackListedError)

    def test_invalid_token(self):
        register(self.client)
        login(self.client)
        headers = dict(Authorization='Bearer invalid.token')
        RestMixin.get(self.client, '/auth/logout', headers=headers)
        self.assertRaises(InvalidTokenError)

    def test_missing_token(self):
        register(self.client)
        login(self.client)
        RestMixin.get(self.client, '/auth/logout')
        self.assertRaises(TokenMissedError)
