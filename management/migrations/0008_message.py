# Generated by Django 3.2.13 on 2022-06-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_alter_reservation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=50, null=True)),
                ('message', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
    ]
