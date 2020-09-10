from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta


class Project(models.Model):
    """
    Represent different type of the Project like Android App,
    Web App, etc..
    """
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='user_engage_projects')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    """
    Represent different type of activity like development, estimation,
    planning, debugging etc..
    """
    name = models.CharField(max_length=255)
    code = models.CharField(
        max_length=5, unique=True,
        help_text='Enter a short code.')

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.code


class Entry(models.Model):
    """
    Represent record a log created by user to track projects.
    """
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='user_entries'
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='entries')
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name='entries')

    class Meta:
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.name

    @property
    def total_duration(self):
        """
        Entry's property for the total duration alloted
        """
        return self.end_time - self.start_time

    @property
    def time_left(self):
        """
        Entry's property for the total duration left
        """
        return self.end_time - timezone.now().replace(microsecond=0)

    @property
    def format_time_left(self):
        """
        Format the time left.
        """
        time = self.end_time + timedelta(hours=5, minutes=30)
        return time.strftime("%m/%d/%Y %H:%M:%S")

    @property
    def time_left_sec(self):
        """
        Format the time left in seconds.
        """
        td = self.time_left
        seconds = td.seconds + td.days * 24 * 3600
        return seconds
