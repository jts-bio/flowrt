# Generated by Django 4.1.1 on 2022-12-23 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0014_slot_template_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='time_pref',
            field=models.CharField(choices=[('AM', 'Morning'), ('MD', 'Midday'), ('PM', 'Evening'), ('XN', 'Overnight')], max_length=10),
        ),
        migrations.AlterField(
            model_name='shift',
            name='group',
            field=models.CharField(choices=[('AM', 'Morning'), ('MD', 'Midday'), ('PM', 'Evening'), ('XN', 'Overnight')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='shifttemplate',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shift_templates', to='sch.employee'),
        ),
        migrations.AlterField(
            model_name='shifttemplate',
            name='shift',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shift_templates', to='sch.shift'),
        ),
    ]
