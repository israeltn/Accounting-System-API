# Generated by Django 4.2.3 on 2024-01-24 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='account_number',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
