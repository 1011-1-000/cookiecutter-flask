from app.common.errors import UserAlreadyExistError
from tests.test_basics import BasicsTestCase
from tests.utils.common import register


class TestUserBlueprint(BasicsTestCase):

    def test_create_user(self):
        response = register(self.client)
        self.assertEqual(response.status_code, 201)

    def test_create_user_exist(self):
        register(self.client)
        response = register(self.client)
        self.assertEqual(response.status_code, 400)
        self.assertRaises(UserAlreadyExistError)
