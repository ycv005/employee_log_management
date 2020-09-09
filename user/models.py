from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.conf import settings


class CustomUserManager(BaseUserManager):
    def create_user(self, name, phone_number, password, email=None):
        if not phone_number:
            raise ValueError("Please Enter a valid Phone number")
        if not password:
            raise ValueError("Please enter a valid password")
        if not name:
            raise ValueError("Please enter a Name")
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, phone_number, password, email=None):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, name, phone_number, password, email=None):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # contacts = models.ManyToManyField(
    #     'self', symmetrical=False, related_name='me_in_other_contacts')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone_number)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class GlobalUser(models.Model):
    phone_number = PhoneNumberField(unique=True)
    spam = models.BooleanField(default=False)
    # contacts = models.ManyToManyField(
    #     'self', symmetrical=False, related_name='me_in_other_contacts')
    contact = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_contacts')

    def __str__(self):
        return str(self.phone_number)


class UserName(models.Model):
    name = models.CharField(max_length=200)
    global_user = models.ForeignKey(
        GlobalUser, on_delete=models.CASCADE, related_name='names')

    def __str__(self):
        return self.name


def global_user_add(sender, instance, *args, **kwargs):
    if instance and not GlobalUser.objects.filter(
            phone_number=instance.phone_number):
        global_user = GlobalUser.objects.create(
            contact=instance,
            phone_number=instance.phone_number,
        )
        UserName.objects.create(
            global_user=global_user,
            name=instance.name
        )


post_save.connect(global_user_add, sender=User)
