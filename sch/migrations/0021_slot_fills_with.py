# Generated by Django 4.1.1 on 2023-01-13 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0020_workday_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='fills_with',
            field=models.ManyToManyField(blank=True, related_name='fills_slots', to='sch.employee'),
        ),
    ]