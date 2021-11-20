# Generated by Django 3.2.8 on 2021-11-20 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('height', models.CharField(max_length=4)),
                ('mass', models.CharField(max_length=5)),
                ('hair_color', models.CharField(max_length=30)),
                ('skin_color', models.CharField(max_length=30)),
                ('eye_color', models.CharField(blank=True, max_length=30)),
                ('birth_year', models.CharField(blank=True, max_length=10)),
                ('gender', models.CharField(blank=True, max_length=15)),
                ('created_date', models.CharField(blank=True, max_length=30)),
                ('updated_date', models.CharField(blank=True, max_length=30)),
                ('url', models.CharField(blank=True, max_length=50)),
                ('characterfakeID', models.CharField(blank=True, max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TravelPlanet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rotation_period', models.CharField(max_length=10)),
                ('diameter', models.CharField(max_length=15)),
                ('climate', models.CharField(max_length=15)),
                ('gravity', models.CharField(max_length=20)),
                ('terrain', models.CharField(max_length=20)),
                ('surface_water', models.CharField(max_length=20)),
                ('population', models.CharField(max_length=20)),
                ('created_date', models.CharField(max_length=20)),
                ('updated_date', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=30)),
                ('planetfakeid', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('user_name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=13)),
                ('fav_character', models.ForeignKey(blank=True, default='Yoda', on_delete=django.db.models.deletion.CASCADE, to='travelpages.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='planet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelpages.travelplanet'),
        ),
    ]
