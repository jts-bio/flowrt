# Generated by Django 4.1.1 on 2022-12-22 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0013_slot_employee duplicates on day'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='template_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='slot_templates', to='sch.employee'),
        ),
    ]
