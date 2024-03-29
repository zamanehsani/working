# Generated by Django 3.1.1 on 2020-11-15 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0023_auto_20201116_0012'),
    ]

    operations = [
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('state_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='start.countries')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='start.countries')),
                ('state', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='start.states')),
            ],
        ),
    ]
