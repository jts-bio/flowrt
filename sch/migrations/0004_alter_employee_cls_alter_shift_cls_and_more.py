# Generated by Django 4.1.1 on 2022-12-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0003_alter_schedule_slug_alter_schedule_version_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='cls',
            field=models.CharField(blank=True, choices=[('CPhT', 'CPhT'), ('RPh', 'RPh')], default='CPhT', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='cls',
            field=models.CharField(choices=[('CPhT', 'CPhT'), ('RPh', 'RPh')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='workday',
            name='slug',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
