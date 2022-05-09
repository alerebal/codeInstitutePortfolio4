# Generated by Django 3.2.13 on 2022-05-09 09:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_item_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
