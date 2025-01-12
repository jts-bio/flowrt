# Generated by Django 4.1.1 on 2022-12-13 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0006_alter_slot_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_pref',
            field=models.CharField(choices=[('Morning', 'AM'), ('Evening', 'PM'), ('Overnight', 'XN')], default='AM', max_length=10),
        ),
        migrations.AlterField(
            model_name='shiftsortpreference',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shiftSortPrefs', to='sch.employee'),
        ),
    ]
