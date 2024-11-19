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
COUNTRY_CHOICES = (
    ('Nepal','Nepal'),
)

PRIMARY_INDUSTRY = (
    ('Software', 'Software'),
    ('Finance', 'Finance'),
    ('Education', 'Education'),
    ('Customer Service', 'Customer Service'),
)

COMPANY_SIZES = (
    ('1 - 5', '1 - 5'),
    ('5 - 35', '5 - 35'),
    ('35 - 65', '35 - 65'),
    ('65 - 105', '65 - 105'),
    ('105 - 205', '105 - 205'),
)
class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    province = models.CharField(max_length=20, choices=PROVINCE_CHOICES)
    country = models.CharField(max_length=20, choices=COUNTRY_CHOICES)
    primary_industry = models.CharField(max_length=100, choices=PRIMARY_INDUSTRY)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=50)
    company_size = models.CharField(max_length=20,choices=COMPANY_SIZES)
    founded_in = models.PositiveIntegerField()
    linkedin = models.URLField()
    website = models.URLField()
    instagram = models.URLField()
    facebook = models.URLField()
    about_company = models.TextField()
