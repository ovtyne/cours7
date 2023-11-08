from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    REGULARITY_CHOICES = (
        ('Daily', 'Eжедневно'),
        ('Monthly', 'Eжемесячно')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь',
                             **NULLABLE)
    place = models.CharField(max_length=255, verbose_name='место')
    time = models.TimeField(verbose_name='время, когда необходимо выполнять')
    action = models.CharField(max_length=255, verbose_name='действие')
    regularity = models.CharField(max_length=7, choices=REGULARITY_CHOICES, default='Daily',
                                  verbose_name='периодичность')
    time_required = models.IntegerField(verbose_name='время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в/на {self.place}.'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'


class PleasantHabit(Habit):
    class Meta:
        verbose_name = 'приятная привычка'
        verbose_name_plural = 'приятные привычки'


class HealthyHabit(Habit):
    related_habit = models.ForeignKey(PleasantHabit, on_delete=models.SET_NULL, **NULLABLE,
                                      verbose_name='связанная привычка')
    reward = models.CharField(max_length=255, verbose_name='награда', **NULLABLE)

    class Meta:
        verbose_name = 'полезная привычка'
        verbose_name_plural = 'полезные привычки'
