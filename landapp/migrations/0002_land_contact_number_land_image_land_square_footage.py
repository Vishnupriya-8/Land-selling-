# Generated by Django 5.1.2 on 2024-10-22 20:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='contact_number',
            field=models.CharField(max_length=20, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='land',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='property_image/'),
        ),
        migrations.AddField(
            model_name='land',
            name='square_footage',
            field=models.IntegerField(default=0),
        ),
    ]
