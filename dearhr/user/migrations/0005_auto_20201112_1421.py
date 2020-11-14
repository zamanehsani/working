# Generated by Django 3.1.1 on 2020-11-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_languages_logging_showcases_skills_visa_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line_1',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='district',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_type',
            name='Type',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='company_type',
            name='category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='endorsments',
            name='user_position',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expereince_role_level',
            name='role_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='coordinates',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='showcases',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
