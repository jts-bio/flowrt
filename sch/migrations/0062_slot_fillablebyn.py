# Generated by Django 4.1.1 on 2022-11-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0061_alter_schedule_number_alter_schedule_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='fillableByN',
            field=models.SmallIntegerField(default=0),
        ),
    ]