# Generated by Django 3.0.6 on 2020-06-23 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='gender',
            field=models.BooleanField(max_length=100, unique=True),
        ),
    ]
