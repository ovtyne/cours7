from django.contrib import admin

from habits.models import HealthyHabit, PleasantHabit


@admin.register(HealthyHabit)
class AdminHealthyHabit(admin.ModelAdmin):
    list_display = ('user', 'action', 'related_habit', 'reward')


@admin.register(PleasantHabit)
class AdminPleasantHabit(admin.ModelAdmin):
    list_display = ('user', 'action')
