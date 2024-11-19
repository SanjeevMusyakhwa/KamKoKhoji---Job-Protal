# Generated by Django 5.1.3 on 2024-11-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_size',
            field=models.CharField(choices=[('1 - 5', '1 - 5'), ('5 - 35', '5 - 35'), ('35 - 65', '35 - 65'), ('65 - 105', '65 - 105'), ('105 - 205', '105 - 205')], max_length=20),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(choices=[('Nepal', 'Nepal')], max_length=20),
        ),
    ]
