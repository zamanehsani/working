# Generated by Django 3.1.1 on 2020-11-15 16:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0021_auto_20201115_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='start.states'),
        ),
        migrations.AlterField(
            model_name='experiences_role_level',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 15, 16, 11, 13, 712227, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='job_type',
            name='date_created',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 11, 15, 16, 11, 13, 711044, tzinfo=utc), null=True),
        ),
    ]
