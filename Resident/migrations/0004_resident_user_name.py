# Generated by Django 5.0.4 on 2024-04-20 20:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        
        ('Resident', '0003_remove_resident_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='user_name',
            field=models.ForeignKey(default='Waqas', on_delete=django.db.models.deletion.CASCADE, to='Account.user'),
            preserve_default=False,
        ),
    ]