# Generated by Django 4.1.1 on 2022-12-21 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0009_alter_employee_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['year', 'number', 'version']},
        ),
    ]
