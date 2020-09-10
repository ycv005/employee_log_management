from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from django.urls import reverse


def validate_start_time(value):
    """
    Validate that a Entry should have a starting date & time in present
    or Future (with 5 Minute negotation)
    """
    if value < timezone.now() - timedelta(minutes=5):
        raise ValidationError(
            "Starting Time should be in present or Future")


def validate_end_time(value):
    """
    Validate that a Entry should have a ending less than 6 months
    """
    print("validating end time")
    if value > timezone.now() + timedelta(days=31*6):
        raise ValidationError(
            "Ending Time should be less than 6 months")


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
    start_time = models.DateTimeField(validators=[validate_start_time])
    end_time = models.DateTimeField(validators=[validate_end_time])
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

    def get_absolute_url(self):
        return reverse('core:entry-detail', kwargs={'pk': self.pk})

    def clean(self):
        """
        Raise Error when a Start time of a Entry > End time of a Entry
        """
        if self.start_time >= self.end_time:
            raise ValidationError("Start time should be less than End Time")

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
        time = self.end_time - timezone.now().replace(microsecond=0)
        if time < timedelta(seconds=1):
            time = timedelta(seconds=0)
        return time

    @property
    def format_time_left(self):
        """
        Format the time left into Day-Hr-Min-Sec
        """
        time = self.end_time + timedelta(hours=5, minutes=30)
        return time.strftime("%m/%d/%Y %H:%M:%S")

    @property
    def is_active(self):
        """
        Check the Expiry of the Entry
        """
        return timezone.now() < self.end_time

    def time_left_sec(self):
        """
        Format the time left in seconds.
        """
        td = self.time_left
        seconds = td.seconds + td.days * 24 * 3600
        return seconds
