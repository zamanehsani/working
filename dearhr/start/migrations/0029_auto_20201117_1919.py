# Generated by Django 3.1.1 on 2020-11-17 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0028_auto_20201117_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiences',
            old_name='local',
            new_name='location',
        ),
    ]
