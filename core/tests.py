from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from .models import Entry, Project, Activity


TEST_USER_CREDENTIAL = {
    "username": "test",
    "email": "test@test.com",
    "password": "testpassword"
}
User = get_user_model()


class EntryModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        """Test data for each test method defined below"""
        self.user = User.objects.create_user(
            **TEST_USER_CREDENTIAL
        )
        self.project = Project.objects.create(
            name='test_proj',

        )
        self.project.users.add(self.user)
        self.activity = Activity.objects.create(
            name='design',
            code='des'
        )

    def test_entry_model(self):
        """
        Test entry model creation
        """
        entry_obj = Entry.objects.create(
            name="test_entry", start_time=timezone.now(),
            end_time=timezone.now() + timedelta(days=1),
            project=self.project, user=self.user, activity=self.activity
        )
        self.assertEquals(str(entry_obj), "test_entry")
        self.assertEquals(Entry.objects.count(), 1)

    def test_entry_start_end_time_great(self):
        """
        Test entry model's field for- start > end time
        """
        try:
            Entry.objects.create(
                name="test_entry", start_time=timezone.now(),
                end_time=timezone.now() - timedelta(days=1),
                project=self.project, user=self.user, activity=self.activity
            )
        except:
            pass
        self.assertEquals(Entry.objects.count(), 0)


class ActivityModelTest(TestCase):
    def test_activity_model(self):
        """
        Test activity model creation
        """
        name = "design"
        code = "des"
        activity_obj = Activity.objects.create(
            name=name,
            code=code
        )
        self.assertEquals(str(activity_obj), code + " - " + name)
        self.assertEquals(Activity.objects.count(), 1)


class ProjectModelTest(TestCase):
    def test_project_model(self):
        """
        Test project model creation
        """
        user = User.objects.create_user(
            **TEST_USER_CREDENTIAL
        )
        project = Project.objects.create(
            name='test_proj',
        )
        project.users.add(user)
        self.assertEquals(str(project), "test_proj")
        self.assertEquals(Project.objects.count(), 1)
