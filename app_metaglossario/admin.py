from django.contrib import admin
from .models import glossary_entry 

from import_export import resources
from import_export.admin import ImportExportModelAdmin


class glossary_entry_resource(resources.ModelResource):
    class Meta:
        model=glossary_entry

class glossary_entry_Admin(ImportExportModelAdmin, admin.ModelAdmin):
    #resource_class = glossary_entry_resource
    pass


# Register your models here.
admin.site.register(glossary_entry, glossary_entry_Admin)







