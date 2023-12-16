from django.urls import path
from . import views
from .views import RegisterUser, LoginUser, logout_user, file_upload, otherForecasts, otherForecast, delete

urlpatterns = [
    path('', views.index, name='home'),
    path('secondPage', file_upload, name='secondPage'),
    path('delete', delete, name='delete'),
    path('otherForecasts', otherForecasts, name='otherForecasts'),
    path('otherForecast', otherForecast, name='otherForecast'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register')
]
