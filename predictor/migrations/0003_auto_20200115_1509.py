# Generated by Django 3.0.2 on 2020-01-15 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictor', '0002_approvals_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approvals',
            name='grade',
            field=models.CharField(max_length=100),
        ),
    ]
