# Generated by Django 4.1.1 on 2022-10-14 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0027_merge_0024_alter_slot_streak_0026_workday_ischedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='employee_class',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='employee_class',
        ),
    ]