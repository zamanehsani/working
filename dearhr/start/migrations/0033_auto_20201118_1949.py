# Generated by Django 3.1.1 on 2020-11-18 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0032_auto_20201118_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='role_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='start.experiences_role_level'),
        ),
        migrations.AlterField(
            model_name='experiences',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='start.job_type'),
        ),
    ]