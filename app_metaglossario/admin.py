from django.contrib import admin
from .models import *

# per il tool import export
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# funzionano ma vs studio li legge male

# per il mkodello di gestione degli utenti
from .models_users_authentication import UserProfileInfo

# queste due funzioni sono collegate al widget import export utilizzabile solo dall'admin

# admin.site.register(prova_oggetto)

# questa classe definita in questo modo mi permette di usare il tool import export
class Controllo_import_export(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
# per ogni modello, registralo con una nuova linea del tipo
# admin.site.register(modello)



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




# i titoli devono rispettare la sintassi modelloAdmin per il custom admin e modelloResource per il custom import export

# ********* glossary_entry *********

# questo modello controlla i field associati al tool import export, non all'admin
class glossary_entryResource(resources.ModelResource):

    class Meta:
        model = glossary_entry
        
        # fields = ('id', 'name', 'price') # per includere i campi
        exclude = ('id',) # per escludere i campi


# modelli admin per la visualizzazione dei modelli aprte admin con funzioni aggiuntive
# questo modello controlla i field associati all'edit dell'admin, non al tool import-export
class glossary_entryAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    resource_class = glossary_entryResource

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']

    # list_display = ['Lemma_it', 'Lemma_ch', 'Id_statico_entry', 'Data_inserimento_entry', 'Admin_approval_switch']
    # list_editable = ['Admin_approval_switch']






# ********* glossary_file *********

class glossary_fileAdmin(admin.ModelAdmin):

    search_fields = ["Glossary_file"]
    list_filter = ['Admin_approval_switch']
    
    # list_display = ['Glossary_file', 'Data_inserimento_glossary', 'Admin_approval_switch']
    # list_editable = ['Admin_approval_switch']

# per uesto modello non è abilitato import export


# ********* acquired_terminology *********

class acquired_terminologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']
    
    # list_display = ['Lemma_it', 'Lemma_ch', 'Id_statico_entry', 'Data_inserimento_entry', 'Admin_approval_switch']
    # list_editable = ['Admin_approval_switch']


# questo modello controlla i field associati al tool import export, non all'admin
class acquired_terminologyResource(resources.ModelResource):

    class Meta:
        model = acquired_terminology
        
        # fields = ('id', 'name', 'price') # per includere i campi
        exclude = ('id') # per escludere i campi



# ********* prepared_terminology *********

class prepared_terminologyAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", 'Data_inserimento_entry','Id_statico_entry','Admin_approval_switch']
    list_filter = ['Admin_approval_switch']
    
    # list_display = ['Lemma_it', 'Lemma_ch', 'Id_statico_entry', 'Data_inserimento_entry', 'Admin_approval_switch']
    # list_editable = ['Admin_approval_switch']

# questo modello controlla i field associati al tool import export, non all'admin
class prepared_terminologyResource(resources.ModelResource):

    class Meta:
        model = prepared_terminology
        
        # fields = ('id', 'name', 'price') # per includere i campi
        exclude = ('id') # per escludere i campi


# registrazione dei modelli per renderli leggibili nella sezione admin
admin.site.register(glossary_entry, glossary_entryAdmin)
admin.site.register(glossary_file, glossary_fileAdmin)
admin.site.register(acquired_terminology, acquired_terminologyAdmin)
admin.site.register(prepared_terminology, prepared_terminologyAdmin)


