# Generated by Django 3.2.8 on 2021-11-20 21:57

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
                ('name', models.CharField(max_length=50, null=True)),
                ('height', models.CharField(max_length=4, null=True)),
                ('mass', models.CharField(max_length=5, null=True)),
                ('hair_color', models.CharField(max_length=30, null=True)),
                ('skin_color', models.CharField(max_length=30, null=True)),
                ('eye_color', models.CharField(blank=True, max_length=30, null=True)),
                ('birth_year', models.CharField(blank=True, max_length=10, null=True)),
                ('gender', models.CharField(blank=True, max_length=15, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('url', models.URLField(null=True)),
                ('character_fake_id', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='TravelPlanet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('rotation_period', models.CharField(max_length=10, null=True)),
                ('orbital_period', models.CharField(default='', max_length=10, null=True)),
                ('diameter', models.CharField(max_length=30, null=True)),
                ('climate', models.CharField(max_length=30, null=True)),
                ('gravity', models.CharField(max_length=100, null=True)),
                ('terrain', models.CharField(max_length=100, null=True)),
                ('surface_water', models.CharField(max_length=100, null=True)),
                ('population', models.CharField(max_length=100, null=True)),
                ('created_date', models.DateTimeField(null=True)),
                ('updated_date', models.DateTimeField(null=True)),
                ('url', models.CharField(max_length=100, null=True)),
                ('planetfakeid', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('dateDepart', models.DateTimeField()),
                ('planet', models.ForeignKey(default='Tatooine', on_delete=django.db.models.deletion.CASCADE, to='travelpages.travelplanet')),
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
            name='planet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelpages.travelplanet'),
        ),
    ]
