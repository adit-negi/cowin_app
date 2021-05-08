from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
class User(AbstractUser):
    EMAIL_VERIFIED = 0
    OTP_VERIFIED = 1
    NOT_VERIFIED = 2


    AUTH_VERIFICATION_STATUS = (
        (EMAIL_VERIFIED, 'Email is verified'),
        (OTP_VERIFIED, 'Phone number is verified'),
        (NOT_VERIFIED, 'Not verified'),

    )

    username = models.CharField(max_length=100, unique=True,  blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(
        upload_to='',  max_length=1000, blank=True, null=True)
    verification_status = models.IntegerField(
        choices=AUTH_VERIFICATION_STATUS, default=3, blank=True, null=True)
# Create your models here.
