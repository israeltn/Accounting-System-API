# Generated by Django 4.2.3 on 2024-02-06 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0002_remove_payroll_doa_remove_payroll_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payroll',
            name='cooptrative',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='ctss',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='gross_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='nhf',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='pension',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='shift_allowance',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='tax',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='total_deductions',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='total_salary',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='payroll',
            name='union_dues',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
