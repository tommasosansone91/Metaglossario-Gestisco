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

Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing FROM (app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing WHERE (((Lemmi.Thing) Like '%acq%') OR ((Acronimi.Thing) Like '%acq%') OR ((Definizioni.Thing) Like '%acq%')) ORDER BY Lemmi.Thing"

#da access a django sql puro

#per evitare confilitti nel like cambia " con '"

#cambia * con %

# i nomi delle tabelle e delle relazioni protrebbero cambiare

# ricerca in tutti i campi acq, metodo OR
# Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing FROM (app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing WHERE (((Lemmi.Thing) Like '%acq%') OR ((Acronimi.Thing) Like '%acq%') OR ((Definizioni.Thing) Like '%acq%')) ORDER BY Lemmi.Thing"

# backup original string
# Query_initial_string = "SELECT Lemmi.Thing, Acronimi.Thing, Definizioni.Thing FROM (app_metaglossario_model_is_Lemma_of INNER JOIN ((app_metaglossario_model_Things AS Acronimi INNER JOIN app_metaglossario_model_is_Acronimo_of ON Acronimi.ID_Thing = app_metaglossario_model_is_Acronimo_of.ID_soggetto) INNER JOIN app_metaglossario_model_Things AS Lemmi ON app_metaglossario_model_is_Acronimo_of.ID_oggetto = Lemmi.ID_Thing) ON app_metaglossario_model_is_Lemma_of.ID_soggetto = Lemmi.ID_Thing) INNER JOIN app_metaglossario_model_Things AS Definizioni ON app_metaglossario_model_is_Lemma_of.ID_oggetto = Definizioni.ID_Thing"



# class QueryFormName(forms.Form):
#     SQL_query = forms.CharField(initial=Query_initial_string, label="") #type your default query here
#     # la label="" come input è per evitare che nel form compaia automaticamente "sql query"

#     # SQL_query = forms.CharField(widget=forms.Textarea, initial=Query_initial_string, label="") #type your default query here
    



