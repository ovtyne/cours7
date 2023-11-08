from django.contrib import admin

from users.models import User


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('email', 'is_active')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.exclude(is_superuser=True)
