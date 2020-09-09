from random import randint
from django.contrib.auth import get_user_model
from .models import GlobalUser, UserName


RANDOM_NAME = ['yash', 'ravi', 'ravish', 'sumit', 'varun', 'kriti',
               'shreya', 'priya', 'supriya', 'ram', 'shyam', 'raman']

TEST_USER_CREDENTIAL = {
    "phone_number": "+918004352531",
    "name": "test",
    "password": "testpassword"
}


def get_test_phone_number():
    digit = 10
    range_start = 10**(digit-1)
    range_end = (10**digit)-1
    n = randint(range_start, range_end)
    return "+91" + str(n)


def get_test_globalusers(number_of_user, user_obj):
    contacts = []
    for i in range(number_of_user):
        n = get_test_phone_number()
        global_user = GlobalUser.objects.create(
            contact=user_obj,
            phone_number=n,
        )
        n = randint(0, len(RANDOM_NAME)-1)
        UserName.objects.create(
            global_user=global_user,
            name=RANDOM_NAME[n]
        )
        n = randint(0, len(RANDOM_NAME)-1)
        UserName.objects.create(
            global_user=global_user,
            name=RANDOM_NAME[n]
        )
        contacts.append(global_user)
    return contacts

def get_test_user(credential=TEST_USER_CREDENTIAL, user='superuser'):
    User = get_user_model()
    if user == 'superuser':
        user_obj = User.objects.create_superuser(**credential)
    else:
        user_obj = User.objects.create_user(**credential)
    return user_obj


def get_test_user_with_global_user(credential, user='superuser'):
    user_obj = get_test_user(credential, user)
    get_test_globalusers(3, user_obj)
    return user_obj


def get_many_test_superusers_or_users(number_of_user, user='superuser'):
    """Create & return number_of_user non-admin user for test"""
    users = []
    for i in range(number_of_user):
        n = get_test_phone_number
        tmp = TEST_USER_CREDENTIAL.copy()
        tmp['phone_number'] = n
        user = get_test_user_with_global_user(tmp, user)
        users.append(user)
    return users
