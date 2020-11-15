# Generated by Django 3.1.1 on 2020-11-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0022_auto_20201115_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='states',
            name='country',
        ),
        migrations.AlterField(
            model_name='experiences_role_level',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='job_type',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
        migrations.DeleteModel(
            name='States',
        ),
    ]
