# Generated by Django 5.0.7 on 2024-07-27 05:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
