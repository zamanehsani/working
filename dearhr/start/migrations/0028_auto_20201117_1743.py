# Generated by Django 3.1.1 on 2020-11-17 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0027_auto_20201117_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiences',
            old_name='local_id',
            new_name='local',
        ),
        migrations.RenameField(
            model_name='experiences',
            old_name='type_id',
            new_name='type',
        ),
    ]
