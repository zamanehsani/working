# Generated by Django 3.1.1 on 2020-11-23 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0040_currency_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='js_job_profile',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='Job_profile/{User.username}'),
        ),
    ]
