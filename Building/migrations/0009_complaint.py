# Generated by Django 5.0.4 on 2024-05-04 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0008_dues_amount_dues_due_date'),
        ('Resident', '0004_remove_resident_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='complaint_images/')),
                ('status', models.CharField(max_length=100)),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Resident.resident')),
                ('society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Building.society')),
            ],
        ),
    ]
