from django.urls import path, include
from .views import index, voluntario,video,punto

urlpatterns = [
     path('', index, name='index'),
     path('registro', voluntario, name='voluntario'),
     path('video', video, name='video'),
     path('punto', punto, name='punto'),
]

                                                                                                                   