from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

PROVINCE_CHOICES = (
    ('province 1', 'Province 1'),
    ('province 2', 'Province 2'),
    ('province 3', 'Province 3'),
    ('province 4', 'Province 4'),
    ('province 5', 'Province 5'),
    ('province 6', 'Province 6'),
    ('province 7', 'Province 7'),
)

EXPERIENCE_CHOICES = (
    ('Freshers', 'Freshers'),
    ('1 - 3', '1 - 3'),
    ('3 - 5', '3 - 5'),
    ('5 - 10', '5 - 10'),
    ('10 - 20', '10 - 20'),
    ('20 - 30', '20 - 30'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

EDUCATION_CHOICES = (
    ('None', 'None'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
    ('Diploma', 'Diploma'),
    ('PHD', 'PHD'),
)

STUDYING_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES)
    country = models.CharField(max_length=20, default='Nepal')
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    language = models.CharField(max_length=20)
    education = models.CharField(max_length=200, choices=EDUCATION_CHOICES)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    about_candidate = models.TextField()

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    course = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    studying = models.CharField(max_length=20, choices=STUDYING_CHOICES, default='No')

class Work(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    role = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    working = models.CharField(max_length=20, choices=STUDYING_CHOICES, default='No')

