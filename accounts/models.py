from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField(unique = True, null=False)
  has_company = models.BooleanField(default=False)
  has_resume = models.BooleanField(default=False)

  is_recruiter = models.BooleanField(default=False)
  is_candidate = models.BooleanField(default=False)
