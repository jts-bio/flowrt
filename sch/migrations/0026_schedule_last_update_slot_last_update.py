# Generated by Django 4.1.1 on 2023-01-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0025_alter_workdayviewpreference_view'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='slot',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
