# Generated by Django 5.1.5 on 2025-05-23 19:34

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_code_expiry_user_verification_code_hash'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='AZ'),
        ),
    ]
