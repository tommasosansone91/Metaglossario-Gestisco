from django.urls import path
from . import views

# viste separate
from . import view_glossario
from . import view_gestione

# viste separate per l'autenticazione degli utenti
from . import views_users_authentication

# serve a permettere il salvataggio dei media
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    
    path('', views.home, name='home'),
    path('indice_glossario', views.indice_glossario, name="indice_glossario"),
    
    path('glossario', view_glossario.glossario, name="glossario"),

    path('aggiungi_terminologia', views.aggiungi_terminologia, name="aggiungi_terminologia"),
    path('aggiungi_terminologia_massa', views.aggiungi_glossario, name="aggiungi_glossario"),
    path('api/glossario', views.api_glossario, name="api_glossario"),
    path('esporta_terminologia', views.esporta_terminologia, name="esporta_terminologia"),       
    
    path('info/che_cos_e_un_metaglossario', views.che_cos_e_un_metaglossario, name="che_cos_e_un_metaglossario"),
    path('info/codice_sorgente', views.codice_sorgente, name="codice_sorgente"),
    path('info/come_sono_organizzati_i_dati', views.come_sono_organizzati_i_dati, name="come_sono_organizzati_i_dati"),    
    path('info/istruzioni_per_l_uso', views.istruzioni_per_l_uso, name="istruzioni_per_l_uso"),
    path('info/bibliografia', views.bibliografia, name="bibliografia"),
    path('info/perche_un_metaglossario', views.perche_un_metaglossario, name="perche_un_metaglossario"),
    path('info/ringraziamenti', views.ringraziamenti, name="ringraziamenti"),


    # user authentication
    path('authentication/registration', views_users_authentication.registration, name="registration"),
    path('authentication/login', views_users_authentication.user_login, name="login"),
    path('logout', views_users_authentication.user_logout, name="logout"),
    path('special', views_users_authentication.special, name="special"),

    # sezione per gli utenti autenticati
    path('tutorial_utenti', view_gestione.tutorial_utenti, name="tutorial_utenti"), 

    # sezione di amministrazione
    path('gestione/pannello_gestione_terminologia', view_gestione.pannello_gestione_terminologia, name="pannello_gestione_terminologia"), 
    path('gestione/istruzioni_gestione_terminologia', view_gestione.istruzioni_gestione_terminologia, name="istruzioni_gestione_terminologia"), 
    path('gestione/tutorial_admin', view_gestione.tutorial_admin, name="tutorial_admin"), 
    
    
]

# path('nome della stringa dell'url', views.nome_funzione_views_associata, name="nome_del_template")

# serve a permettere il salvataggio dei media
# lo metto qui perchè voglio fare una cosa ordinata, nel tutorial viene messo nell'uls.py di Metaglssaio_Gestisco

# se i settings sono in debug mode (cioè in developement)
# non andrebbe usato in produzione
# ma vuol dire che in developement e produzione mi usa due location di salvataggio diverse?
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
