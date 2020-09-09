from django.test import TestCase
from django.contrib.auth import get_user_model
from user.helper import (
    get_test_user_with_global_user, get_many_test_superusers_or_users, get_test_phone_number)
from user.models import GlobalUser, UserName

TEST_USER_CREDENTIAL = {
    "phone_number": "+918004352531",
    "name": "test",
    "password": "testpassword"
}
User = get_user_model()


class UserRelatedModelTest(TestCase):
    def test_user_related_model(self):
        """Test user, global user, username model creation"""
        user_obj = User.objects.create_user(**TEST_USER_CREDENTIAL)
        self.assertEquals(str(user_obj), TEST_USER_CREDENTIAL["phone_number"])
        self.assertEquals(User.objects.count(), 1)

        self.assertEquals(GlobalUser.objects.count(), 1)

        self.assertEquals(UserName.objects.count(), 1)
