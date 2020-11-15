# Generated by Django 3.1.1 on 2020-11-15 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0010_auto_20201115_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='country_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cities',
            name='state_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='iso2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='countries',
            name='iso3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='experiences_role_level',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 15, 14, 10, 14, 591087, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='job_type',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 15, 14, 10, 14, 591087, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='country_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='states',
            name='state_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]