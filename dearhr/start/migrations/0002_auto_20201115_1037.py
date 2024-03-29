# Generated by Django 3.1.1 on 2020-11-15 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('start', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('code', models.CharField(max_length=5, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user_profile',
            name='DOB',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('Job Seeker', 'Job Seeker'), ('HR', 'HR'), ('Service Provider', 'Service Provider')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='mationality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='start.countries'),
        ),
    ]
