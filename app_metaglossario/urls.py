from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns=[
    path('', views.home, name='home'),
    path('aggiungi_terminologia', views.aggiungi_terminologia, name="aggiungi_terminologia"),
    path('glossario', views.glossario, name="glossario"),
]