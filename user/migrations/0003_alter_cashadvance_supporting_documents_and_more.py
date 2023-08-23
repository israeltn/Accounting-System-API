# Generated by Django 4.2.3 on 2023-08-19 16:01

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_capital_alter_cashadvance_supporting_documents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashadvance',
            name='supporting_documents',
            field=models.FileField(null=True, upload_to='cash_advance/', validators=[user.models.validate_image_size]),
        ),
        migrations.AlterField(
            model_name='retirementvoucher',
            name='supporting_documents',
            field=models.FileField(null=True, upload_to='retirement_voucher/', validators=[user.models.validate_image_size]),
        ),
    ]
