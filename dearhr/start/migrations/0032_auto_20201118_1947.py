# Generated by Django 3.1.1 on 2020-11-18 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0031_auto_20201117_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiences',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='start.countries'),
        ),
    ]
