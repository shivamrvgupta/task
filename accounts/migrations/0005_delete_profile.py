# Generated by Django 4.1.5 on 2023-01-16 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_profile_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
