# Generated by Django 3.0.2 on 2020-01-15 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0003_auto_20200115_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='approvals',
            name='grade',
        ),
    ]
