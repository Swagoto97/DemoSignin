from django.db import models
from django.contrib.auth.models import User
from datetime import *

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "Profile"
