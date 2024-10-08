# Generated by Django 4.2.3 on 2024-01-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashadvance', '0003_alter_cashadvance_is_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashadvance',
            name='is_approved',
            field=models.CharField(choices=[('processing', 'Processing'), ('approved', 'Approved'), ('audited', 'Audited'), ('reviewed', 'Reviewed'), ('paid', 'Paid')], default='processing', max_length=20),
        ),
    ]
