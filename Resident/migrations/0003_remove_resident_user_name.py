# Generated by Django 5.0.4 on 2024-04-20 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Resident', '0002_alter_resident_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resident',
            name='user_name',
        ),
    ]
