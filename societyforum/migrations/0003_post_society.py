# Generated by Django 5.0.4 on 2024-05-01 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0005_remove_amenities_maintenance_amenities_building_and_more'),
        ('societyforum', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='society',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Building.society'),
            preserve_default=False,
        ),
    ]