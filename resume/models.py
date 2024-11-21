from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
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
    ('SEE', 'SEE'),
    ('SLC', 'SLC'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
    ('Diploma', 'Diploma'),
    ('PHD', 'PHD'),
)

STUDYING_CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No'),
)

MARITAL_STATUS = (
    ('Single','Single'),
    ('Married','Married'),
    ('Divorced','Divorced'),
    ('Widow','Widow'),
)
class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()  # Changed to DateField
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    language = models.CharField(max_length=50)  # Increased max_length for multilingual capabilities
    about_candidate = models.TextField()
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES)
    country = models.CharField(max_length=20, default='Nepal')
    phone_number = models.CharField(max_length=13)  # Removed max_length from PositiveIntegerField
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=300)
    experience = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES)
    education = models.CharField(max_length=200, choices=EDUCATION_CHOICES)
    

    def __str__(self):
        return f"Resume of {self.user.username}"
    
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    course = models.CharField(max_length=50, default='None')
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    studying = models.CharField(max_length=20, choices=STUDYING_CHOICES, default='No')
    school_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.degree} at {self.school_name}"

class Work(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    role = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    working = models.CharField(max_length=20, choices=STUDYING_CHOICES, default='No')

