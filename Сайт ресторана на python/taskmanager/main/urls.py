from django.conf.urls.static import static
from django.urls import path, include
from taskmanager import settings

from . import views

# смотрим при переходе на какую страницу и вызываем функцию из views.
from .views import pageNotFound
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='menu'),
    path('about', views.about, name='about'),
    path('spisokbroni', views.spisokbroni, name='spisokbroni'),
    path('createforum', views.createforum, name='createforum'),
    path('actions', views.actions, name='actions'),
    path('pizza', views.pizza, name='pizza'),
    path('rolls', views.rolls, name='rolls'),
    path('sushi', views.sushi, name='sushi'),
    path('drinks', views.drinks, name='drinks'),
    path('politika', views.politika, name='politika'),
    path('work', views.work, name='work'),
    path('workspisok', views.workspisok, name='workspisok'),
    path('booktable', views.booktable, name='booktable'),
    path('new', views.new, name='new'),
    path('', include('loginsys.urls')),
    path('', include('loginsys.urls')),
    path('profil', views.profil, name='profil'),
    path('forum', views.forum, name='forum'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
