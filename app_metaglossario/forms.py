from django import forms
from .models import glossary_entry
from .models import glossary_file


class glossary_entry_form(forms.ModelForm):
                
    class Meta:
        model = glossary_entry
        fields = ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]


class glossary_file_form(forms.ModelForm):

    class Meta:
        model = glossary_file
        fields = ["Glossary_file", "Data_inserimento_glossary"]


##### form del metaglossario

Query_initial_string = "SELECT things_2.Thing AS Acronimo, things_3.Thing AS Definizione, [model_Things].Thing AS Ambito_riferimento, things_4.Thing AS autore_def, things_6.Thing AS url_def, things_7.Thing AS titolo_doc, things_8.Thing AS autore_doc, things_9.Thing AS URL_doc, things_10.Thing AS Host_doc, things_1.Thing AS Lemma FROM (model_Things AS things_1 INNER JOIN ((model_Things AS things_9 INNER JOIN model_is_Url_documento_fonte_of ON things_9.ID_Thing=[model_is_Url_documento_fonte_of].ID_soggetto) INNER JOIN ((model_Things AS things_10 INNER JOIN model_is_Host_documento_fonte_of ON things_10.ID_Thing=[model_is_Host_documento_fonte_of].ID_soggetto) INNER JOIN ((model_Things AS things_8 INNER JOIN model_is_Autore_documento_of ON things_8.ID_Thing=[model_is_Autore_documento_of].ID_soggetto) INNER JOIN ((model_Things INNER JOIN model_is_Ambito_riferimento_of ON [model_Things].ID_Thing=[model_is_Ambito_riferimento_of].ID_soggetto) INNER JOIN ((((model_Things AS things_4 INNER JOIN ((model_is_Lemma_of INNER JOIN model_Things AS things_3 ON [model_is_Lemma_of].ID_oggetto=things_3.ID_Thing) INNER JOIN model_is_Autore_definizione_of ON things_3.ID_Thing=[model_is_Autore_definizione_of].ID_oggetto) ON things_4.ID_Thing=[model_is_Autore_definizione_of].ID_soggetto) INNER JOIN (model_Things AS things_6 INNER JOIN model_is_Url_definizione_of ON things_6.ID_Thing=[model_is_Url_definizione_of].ID_soggetto) ON things_3.ID_Thing=[model_is_Url_definizione_of].ID_oggetto) INNER JOIN (model_Things AS things_5 INNER JOIN model_is_Posizione_definizione_of ON things_5.ID_Thing=[model_is_Posizione_definizione_of].ID_soggetto) ON things_3.ID_Thing=[model_is_Posizione_definizione_of].ID_oggetto) INNER JOIN (model_is_Titolo_documento_fonte_of INNER JOIN model_Things AS things_7 ON [model_is_Titolo_documento_fonte_of].ID_soggetto=things_7.ID_Thing) ON things_3.ID_Thing=[model_is_Titolo_documento_fonte_of].ID_oggetto) ON [model_is_Ambito_riferimento_of].ID_oggetto=things_3.ID_Thing) ON [model_is_Autore_documento_of].ID_oggetto=things_7.ID_Thing) ON [model_is_Host_documento_fonte_of].ID_oggetto=things_7.ID_Thing) ON [model_is_Url_documento_fonte_of].ID_oggetto=things_7.ID_Thing) ON things_1.ID_Thing=[model_is_Lemma_of].ID_soggetto) INNER JOIN (model_Things AS things_2 INNER JOIN model_is_Acronimo_of ON things_2.ID_Thing=[model_is_Acronimo_of].ID_soggetto) ON things_1.ID_Thing=[model_is_Acronimo_of].ID_oggetto ORDER BY things_1.Thing;"

# check out this
# app_metaglossario_model_things

class QueryFormName(forms.Form):
    SQL_query = forms.CharField(widget=forms.Textarea, initial=Query_initial_string, label="") #type your default query here
    # la label="" come input è per evitare che nel form compaia automaticamente "sql query"



