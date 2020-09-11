from django.test import TestCase
from django.contrib.auth import get_user_model


TEST_USER_CREDENTIAL = {
    "username": "test",
    "email": "test@test.com",
    "password": "testpassword"
}

User = get_user_model()


class UserModelTest(TestCase):
    def test_user_model(self):
        """
        Test user model creation
        """
        user_obj = User.objects.create_user(**TEST_USER_CREDENTIAL)
        self.assertEquals(str(user_obj), TEST_USER_CREDENTIAL["email"])
        self.assertEquals(User.objects.count(), 1)
