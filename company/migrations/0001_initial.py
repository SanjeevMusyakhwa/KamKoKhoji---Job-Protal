# Generated by Django 5.1.3 on 2024-11-21 08:59

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
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('website', models.URLField()),
                ('founded_in', models.PositiveIntegerField()),
                ('primary_industry', models.CharField(choices=[('Software', 'Software'), ('Finance', 'Finance'), ('Education', 'Education'), ('Customer Service', 'Customer Service')], max_length=100)),
                ('province', models.CharField(choices=[('province 1', 'Province 1'), ('province 2', 'Province 2'), ('province 3', 'Province 3'), ('province 4', 'Province 4'), ('province 5', 'Province 5'), ('province 6', 'Province 6'), ('province 7', 'Province 7')], max_length=20)),
                ('company_size', models.CharField(choices=[('1 - 5', '1 - 5'), ('5 - 35', '5 - 35'), ('35 - 65', '35 - 65'), ('65 - 105', '65 - 105'), ('105 - 205', '105 - 205')], max_length=20)),
                ('country', models.CharField(choices=[('Nepal', 'Nepal')], max_length=20)),
                ('linkedin', models.URLField()),
                ('instagram', models.URLField()),
                ('facebook', models.URLField()),
                ('about_company', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
