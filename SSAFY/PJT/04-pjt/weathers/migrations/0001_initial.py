# Generated by Django 4.2.16 on 2024-09-27 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('TempHighF', models.IntegerField()),
                ('TempAvgF', models.IntegerField()),
                ('TempLowF', models.IntegerField()),
                ('DewPointHighF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('DewPointAvgF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('DewPointLowF', models.DecimalField(decimal_places=5, max_digits=10)),
                ('HumidityHighPercent', models.DecimalField(decimal_places=5, max_digits=10)),
                ('HumidityAvgPercent', models.DecimalField(decimal_places=5, max_digits=10)),
                ('HumidityLowPercent', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SeaLevelPressureHighInches', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SeaLevelPressureAvgInches', models.DecimalField(decimal_places=5, max_digits=10)),
                ('SeaLevelPressureLowInches', models.DecimalField(decimal_places=5, max_digits=10)),
                ('VisibilityHighMiles', models.IntegerField()),
                ('VisibilityAvgMiles', models.IntegerField()),
                ('VisibilityLowMiles', models.IntegerField()),
                ('WindHighMPH', models.IntegerField()),
                ('WindAvgMPH', models.IntegerField()),
                ('WindGustMPH', models.IntegerField()),
                ('PrecipitationSumInches', models.CharField(max_length=255)),
                ('Events', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]