from django.contrib import admin
from .models import glossary_entry 
from .models import glossary_file

from import_export import resources
from import_export.admin import ImportExportModelAdmin
# funzionano ma vs studio li legge male

# queste due funzioni sono collegate al widget import export utilizzabile solo dall'admin

class glossary_entry_resource(resources.ModelResource):
    class Meta:
        model=glossary_entry
        # fields = ('id', 'name', 'price',) # per includere i campi
        # exclude = ('id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ) # per escludere i campi

class glossary_entry_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = glossary_entry_resource
    pass





# Register your models here.
# per ogni modello, registralo con una nuova linea del tipo
# admin.site.register(modello)

admin.site.register(glossary_entry, glossary_entry_Admin)

# solo il modello accoppiato ad import-export prende in ingresso un secondo argomento quando registrato,
# il secondo argomento è la funzione admin in cui in realtà viene messo pass

admin.site.register(glossary_file)







