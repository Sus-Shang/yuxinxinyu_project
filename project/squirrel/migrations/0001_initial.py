# Generated by Django 3.1.2 on 2020-10-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='Latitude value', max_length=50)),
                ('longitude', models.FloatField(help_text='Longitude value', max_length=50)),
                ('unique_squirrel_ID', models.CharField(help_text='Squirrel_ID', max_length=50)),
                ('shift', models.CharField(choices=[('PM', 'PM'), ('AM', 'AM'), ('Other', 'Other')], default='Other', max_length=15)),
                ('date', models.DateField(help_text='The date you saw the squirrel')),
                ('age', models.CharField(choices=[('Adult', 'adult'), ('Juvenile', 'juvenile'), ('Other', 'Other')], default='Other', max_length=15)),
                ('primary_fur_color', models.CharField(choices=[('Black', 'Black'), ('Cinnamon', 'Cinnamon'), ('Gray', 'Gray'), ('Other', 'Other')], default='Other', max_length=50)),
                ('location', models.CharField(choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground'), ('Other', 'Blank or other')], default='Other', max_length=100)),
                ('specific_location', models.CharField(blank=True, help_text='Specific Location', max_length=500)),
                ('running', models.BooleanField(default=False, help_text='Running?')),
                ('chasing', models.BooleanField(default=False, help_text='Chasing?')),
                ('climbing', models.BooleanField(default=False, help_text='Climbing?')),
                ('eating', models.BooleanField(default=False, help_text='Eating?')),
                ('foraging', models.BooleanField(default=False, help_text='Foraging?')),
                ('other_activities', models.CharField(blank=True, help_text='Specific Location', max_length=500)),
                ('kuks', models.BooleanField(default=False, help_text='Kuks?')),
                ('quaas', models.BooleanField(default=False, help_text='Quaas?')),
                ('moans', models.BooleanField(default=False, help_text='Moans?')),
                ('tail_flags', models.BooleanField(default=False, help_text='Tail Flags?')),
                ('tail_twitches', models.BooleanField(default=False, help_text='Tail twitches?')),
                ('approaches', models.BooleanField(default=False, help_text='Approaches?')),
                ('indifferent', models.BooleanField(default=False, help_text='Indifferent?')),
                ('runs_from', models.BooleanField(default=False, help_text='Runs from?')),
                ('other_interactions', models.CharField(blank=True, help_text='Other Interactions?', max_length=500)),
            ],
        ),
    ]
