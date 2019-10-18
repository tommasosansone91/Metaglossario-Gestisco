from django.urls import path
from . import views

# serve a permettere il salvataggio dei media
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.home, name='home'),
    path('aggiungi_terminologia', views.aggiungi_terminologia, name="aggiungi_terminologia"),
    path('glossario', views.glossario, name="glossario"),
    path('aggiungi_glossario', views.aggiungi_glossario, name="aggiungi_glossario"),
]

# serve a permettere il salvataggio dei media
# lo metto qui perchè voglio fare una cosa ordinata, nel tutorial viene messo nell'uls.py di Metaglssaio_Gestisco

# se i settings sono in debug mode (cioè in developement)
# non andrebbe usato in produzione
# ma vuol dire che in developement e produzione mi usa due location di salvataggio diverse?
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
