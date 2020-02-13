from django.contrib import admin
from .models import *

# per il tool import export
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# funzionano ma vs studio li legge male

# per il mkodello di gestione degli utenti
from .models_users_authentication import UserProfileInfo

# queste due funzioni sono collegate al widget import export utilizzabile solo dall'admin

class glossary_entry_resource(resources.ModelResource):

    class Meta:
        model = glossary_entry
        
        # fields = ('id', 'name', 'price') # per includere i campi
        exclude = ['id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ] # per escludere i campi

# questa classe definita in questo modo mi permette di usare il tool import export
class Controllo_import_export(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
# per ogni modello, registralo con una nuova linea del tipo
# admin.site.register(modello)


admin.site.register(glossary_file)
# non serve fare import export di gruppi di interi files... non è possibile

# questa scrittura mi permetteva di usare il tool import export
# admin.site.register(glossary_entry, Controllo_import_export)
# admin.site.register(acquired_terminology, Controllo_import_export)
# admin.site.register(prepared_terminology, Controllo_import_export)
# ho dovuto commentarla perchè per usare le funzioni estese dell'admin
# avrei dovito registrare due volte il modello e invece non posso farlo
# ho risolto mettendo negli argomenti di ereditazione delle classi 
# (ImportExportModelAdmin, admin.ModelAdmin)
# e poi cancellando la vecchia nomenclatura

# solo il modello accoppiato ad import-export prende in ingresso un secondo argomento quando registrato,
# il secondo argomento è la funzione admin in cui in realtà viene messo pass

# registrare il modello delle info degli utenti
admin.site.register(UserProfileInfo)



# modelli admin per la visualizzazione dei modelli aprte admin con funzioni aggiuntive
class glossary_entryAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']


class acquired_terminologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']


class prepared_terminologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']




admin.site.register(glossary_entry, glossary_entryAdmin)
admin.site.register(acquired_terminology, acquired_terminologyAdmin)
admin.site.register(prepared_terminology, prepared_terminologyAdmin)


