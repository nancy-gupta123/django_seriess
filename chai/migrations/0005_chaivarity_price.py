# Generated by Django 5.0.7 on 2024-07-27 12:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0004_chaivarity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarity',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=1000, validators=[django.core.validators.MinValueValidator(149), django.core.validators.MaxValueValidator(1000)]),
        ),
    ]
