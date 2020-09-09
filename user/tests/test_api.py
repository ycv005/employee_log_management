from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from user.helper import get_test_user, get_test_phone_number
from user.models import GlobalUser


USERLIST_URL = reverse('user-list')
GLOBALLIST_URL = reverse('globaluser-list')


def get_detail_user_url(id):
    return reverse('globaluser-detail', args=[id])


def get_detail_global_url(id):
    return reverse('globaluser-detail', args=[id])


class PublicDataTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        self.client = APIClient()

    def test_public_data_user_list_side(self):
        """Test the public data availability on user list"""
        res = self.client.get(USERLIST_URL)
        self.assertEquals(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_public_data_user_detail_side(self):
        """Test the public data availability on user detail"""
        user_obj = get_test_user()
        res = self.client.get(get_detail_user_url(user_obj.id))
        self.assertEquals(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_public_data_globaluser_list(self):
        """Test the public data availability on global side"""
        res = self.client.get(GLOBALLIST_URL)
        self.assertEquals(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_public_data_globaluser_detail(self):
        """Test the public data availability on globaluser detail"""
        user_obj = get_test_user()
        global_user = GlobalUser.objects.get(contact=user_obj)
        res = self.client.get(get_detail_global_url(global_user.id))
        self.assertEquals(res.status_code, status.HTTP_403_FORBIDDEN)


class PrivateDataTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_test_user()
        self.client.force_authenticate(self.user)
        self.global_user = GlobalUser.objects.get(contact=self.user)

    def test_user_list(self):
        """Test to retrieve all user list"""
        res = self.client.get(USERLIST_URL)
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        """Test to retrieve user detail"""
        res = self.client.get(get_detail_user_url(self.user.id))
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_globaluser_list(self):
        """Test to retrieve all globaluser list"""
        res = self.client.get(GLOBALLIST_URL)
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_user_detail(self):
        """Test to retrieve user detail"""
        res = self.client.get(get_detail_global_url(self.global_user.id))
        self.assertEquals(res.status_code, status.HTTP_200_OK)

    def test_mark_user_spam(self):
        """Test to mark any user as a spammer"""
        data = {
            "phone_number": get_test_phone_number(),
            "contact": self.user
        }
        global_user_1 = GlobalUser.objects.create(
            **data
        )
        self.assertFalse(global_user_1.spam)
        res = self.client.put(get_detail_global_url(
            global_user_1.id), data=data)
        global_user_1.refresh_from_db()
        self.assertTrue(global_user_1.spam)
