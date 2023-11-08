from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.apps import UsersConfig
from users.views import RegistrationApiView

app_name = UsersConfig.name

urlpatterns = [
   path('register/', RegistrationApiView.as_view(), name='register'),
   path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
