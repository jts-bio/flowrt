# Generated by Django 4.1.1 on 2022-12-22 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0012_remove_slot_shift duplicates on day_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='slot',
            constraint=models.UniqueConstraint(fields=('workday', 'employee', 'schedule'), name='Employee Duplicates on day'),
        ),
    ]
