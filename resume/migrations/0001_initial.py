# Generated by Django 5.1.3 on 2025-02-08 04:25

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widow', 'Widow')], max_length=20)),
                ('language', models.CharField(max_length=50)),
                ('about_candidate', models.TextField()),
                ('province', models.CharField(choices=[('province 1', 'Province 1'), ('province 2', 'Province 2'), ('province 3', 'Province 3'), ('province 4', 'Province 4'), ('province 5', 'Province 5'), ('province 6', 'Province 6'), ('province 7', 'Province 7')], max_length=20)),
                ('country', models.CharField(default='Nepal', max_length=20)),
                ('phone_number', models.CharField(max_length=13)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('address', models.CharField(max_length=300)),
                ('experience', models.CharField(choices=[('Freshers', 'Freshers'), ('1 - 3', '1 - 3'), ('3 - 5', '3 - 5'), ('5 - 10', '5 - 10'), ('10 - 20', '10 - 20'), ('20 - 30', '20 - 30')], max_length=20)),
                ('education', models.CharField(choices=[('None', 'None'), ('SEE', 'SEE'), ('SLC', 'SLC'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Diploma', 'Diploma'), ('PHD', 'PHD')], max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(choices=[('None', 'None'), ('SEE', 'SEE'), ('SLC', 'SLC'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Diploma', 'Diploma'), ('PHD', 'PHD')], max_length=20)),
                ('course', models.CharField(max_length=50)),
                ('start_year', models.PositiveIntegerField()),
                ('end_year', models.PositiveIntegerField()),
                ('studying', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('school_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('proficiency_level', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('start_year', models.PositiveIntegerField()),
                ('end_year', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=255)),
                ('working', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='resume.resume')),
            ],
        ),
    ]
