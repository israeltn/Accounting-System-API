# Generated by Django 4.2.3 on 2024-01-30 08:27

import capital.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capital', '0030_alter_capital_supporting_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capital',
            name='supporting_documents',
            field=models.FileField(null=True, upload_to='capital/', validators=[capital.models.validate_image_size]),
        ),
    ]
