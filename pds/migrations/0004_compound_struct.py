# Generated by Django 4.1.1 on 2023-01-04 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0003_alter_diluent_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='struct',
            field=models.JSONField(default={'': ''}),
            preserve_default=False,
        ),
    ]
