from django.contrib import admin
from .models import glossary_entry 

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class glossary_entry_resource(resources.ModelResource):
    class Meta:
        model=glossary_entry
        # fields = ('id', 'name', 'price',) # per includere i campi
        # exclude = ('id','Data_inserimento_entry','Id_statico_entry','Admin_approval_switch' ) # per escludere i campi

class glossary_entry_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    # resource_class = glossary_entry_resource
    pass





# Register your models here.
admin.site.register(glossary_entry, glossary_entry_Admin)







