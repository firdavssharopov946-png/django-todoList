from django.db import models # noqa
from django.contrib.auth.models import AbstractUser # noqa


# Create your models here.
class User(AbstractUser):

    def __str__(self):
        return f"{self.username}"
