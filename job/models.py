from django.db import models
from django.contrib.auth import get_user_model
from company.models import Company

User = get_user_model()

PAY_MODE = (
    ('Daily', 'Daily'),
    ('Weekly', 'Weekly'),
    ('Monthly', 'Monthly'),
)

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

JOB_LOCATION = (
    ('Remote', 'Remote'),
    ('Hybrid', 'Hybrid'),
    ('Onsite', 'Onsite'),
)

JOB_CATEGORY = (
    ('Permanent', 'Permanent'),
    ('Contract', 'Contract'),
)
STATUS = (
    ('Pending','Pending'),
    ('Active','Active'),
    ('Expired','Expired'),
)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Renamed for clarity
    title = models.CharField(max_length=200)
    post_date_time = models.DateTimeField(auto_now_add=True, editable=False)
    date_posted = models.DateField(auto_now_add=True)
    salary = models.PositiveIntegerField()
    pay_mode = models.CharField(max_length=20, choices=PAY_MODE)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE)
    job_location = models.CharField(max_length=200, choices=JOB_LOCATION)
    job_category = models.CharField(max_length=200, choices=JOB_CATEGORY)
    expiry_date = models.DateTimeField(null=True, blank=True)
    job_description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default='Pending')

    def __str__(self):
        return self.title

class JobResponsibility(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Responsibility: {self.name} for {self.job.title}"

class JobExperience(models.Model):  # Corrected the typo
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Experience: {self.name} for {self.job.title}"
