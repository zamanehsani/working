# Generated by Django 3.1.1 on 2020-11-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0039_currency_job_profile_edu_job_profile_endors_job_profile_exp_job_profile_show_job_profile_skill_js_jo'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='number',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]