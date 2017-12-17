# Generated by Django 2.0 on 2017-12-17 00:39

from django.db import migrations, models
import vehicle.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('sub_model', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=120, validators=[vehicle.validators.validate_category])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
    ]