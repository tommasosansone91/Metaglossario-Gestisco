from django.contrib import admin
from .models import glossary_entry 
from .models import glossary_file
from .models import acquired_terminology
from .models import prepared_terminology
# from .models import displaying_terminology

# importa tutti i modelli del metaglossario
from app_metaglossario.metaglossary_models import *

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

# altri modelli che registro normalmente

admin.site.register(glossary_file)
admin.site.register(acquired_terminology)
admin.site.register(prepared_terminology)
# admin.site.register(displaying_terminology)

# qui registro i modelli del metaglossario

admin.site.register(model_Things)
admin.site.register(model_is_Acronimo_of)
admin.site.register(model_is_Lemma_of)
admin.site.register(model_is_Ambito_riferimento_of)
admin.site.register(model_is_Autore_definizione_of)
admin.site.register(model_is_Posizione_definizione_of)
admin.site.register(model_is_Url_definizione_of)
admin.site.register(model_is_Titolo_documento_fonte_of)
admin.site.register(model_is_Autore_documento_fonte_of)
admin.site.register(model_is_Url_documento_fonte_of)
admin.site.register(model_is_Commento_entry_of)
admin.site.register(model_is_Data_inserimento_entry_of)
admin.site.register(model_is_Id_statico_entry_of)
admin.site.register(model_is_Admin_approval_switch_of)






