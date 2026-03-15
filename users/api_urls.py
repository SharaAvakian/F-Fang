from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', api_views.RegisterView.as_view(), name='api_register'),
    path('me/', api_views.UserDetailView.as_view(), name='api_me'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
