from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company
# Create your models here.

User = get_user_model()


PAY_MODE = (
  ('Daily', 'Daily'),
  ('Weekly', 'Weekly'),
  ('Monthly', 'Monthly'),
)

JOB_TYPE = (
  ('Full Time','Full Time'),
  ('Part Time','Part Time'),
)

JOB_LOCATION = (
  ('Remote','Remote'),
  ('Hybrid','Hybrid'),
  ('Onsite','Onsite'),
)

JOB_CATEGORY = (
  ('Permanent','Permanent'),
  ('Contract','Contract'),
)
class Job(models.Model):
  user = models.ForeignKey(Company,  on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  post_date_time = models.DateTimeField(auto_now_add=True)
  date_posted = models.DateField(auto_now_add=True)
  salary = models.PositiveIntegerField()
  pay_mode = models.CharField(max_length=20, choices=PAY_MODE)
  job_type = models.CharField(max_length=50, choices=JOB_TYPE)
  job_location = models.CharField(max_length=200, choices=JOB_LOCATION)
  job_category = models.CharField(max_length=200, choices=JOB_CATEGORY )
  expiry_date = models.DateTimeField(null= True)
  job_description = models.TextField()



class JobResponsibility(models.Model):
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  name = models.CharField(max_length=300)


class JobExperiecnce(models.Model):
  job = models.ForeignKey(Job, on_delete=models.CASCADE)
  name = models.CharField(max_length=300)
