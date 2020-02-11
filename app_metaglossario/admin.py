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
        
        fields = ('id', 'name', 'price',) # per includere i campi
        exclude = ('id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ) # per escludere i campi

# questa classe definita in questo modo mi permette di usare il tool import export
class Controllo_import_export(ImportExportModelAdmin, admin.ModelAdmin):
    pass


# Register your models here.
# per ogni modello, registralo con una nuova linea del tipo
# admin.site.register(modello)


admin.site.register(glossary_file)


# questa scrittura mi permette di usare il tool import export
admin.site.register(glossary_entry, Controllo_import_export)
admin.site.register(acquired_terminology, Controllo_import_export)
admin.site.register(prepared_terminology, Controllo_import_export)

# solo il modello accoppiato ad import-export prende in ingresso un secondo argomento quando registrato,
# il secondo argomento è la funzione admin in cui in realtà viene messo pass

# registrare il modello delle info degli utenti
admin.site.register(UserProfileInfo)







