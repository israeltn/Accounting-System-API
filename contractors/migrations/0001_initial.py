# Generated by Django 4.2.3 on 2024-01-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('tin_number', models.CharField(max_length=20, unique=True)),
                ('bank', models.CharField(max_length=255)),                
                ('sort_code', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('services_offered', models.TextField()),
            ],
        ),
    ]
