# Generated by Django 3.1.1 on 2020-11-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0003_auto_20201115_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='marriatal_status',
            field=models.CharField(blank=True, choices=[('Signle', 'Single'), ('Marriaged', 'Marriaged'), ('Devorced', 'Devorced')], max_length=50, null=True),
        ),
    ]