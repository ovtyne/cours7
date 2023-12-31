# Generated by Django 4.2.7 on 2023-11-08 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=255, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время, когда необходимо выполнять')),
                ('action', models.CharField(max_length=255, verbose_name='действие')),
                ('regularity', models.CharField(choices=[('Daily', 'Eжедневно'), ('Monthly', 'Eжемесячно')], default='Daily', max_length=7, verbose_name='периодичность')),
                ('time_required', models.IntegerField(verbose_name='время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
        migrations.CreateModel(
            name='HealthyHabit',
            fields=[
                ('habit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='habits.habit')),
                ('reward', models.CharField(blank=True, max_length=255, null=True, verbose_name='награда')),
            ],
            options={
                'verbose_name': 'полезная привычка',
                'verbose_name_plural': 'полезные привычки',
            },
            bases=('habits.habit',),
        ),
        migrations.CreateModel(
            name='PleasantHabit',
            fields=[
                ('habit_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='habits.habit')),
            ],
            options={
                'verbose_name': 'приятная привычка',
                'verbose_name_plural': 'приятные привычки',
            },
            bases=('habits.habit',),
        ),
    ]
