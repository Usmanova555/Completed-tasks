from django.urls import path
from . import views

urlpatterns = [
    path('', views.forecasts_home, name='forecasts_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.ForecastsDetailViews.as_view(), name='forecasts-detail'),
    path('<int:pk>/update', views.ForecastsUpdateViews.as_view(), name='forecasts-update'),
    path('<int:pk>/delete', views.ForecastsDeleteViews.as_view(), name='forecasts-delete'),
]

