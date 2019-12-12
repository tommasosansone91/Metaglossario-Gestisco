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

Query_initial_string = "SELECT things_2.thing AS Acronimo, things_3.thing AS Definizione, things.thing AS Ambito, things_4.thing AS autore_def, things_6.thing AS url_def, things_7.thing AS titolo_doc, things_8.thing AS autore_doc, things_9.thing AS URL_doc, things_10.thing AS Host_doc, things_1.thing AS Lemma FROM (things AS things_1 INNER JOIN ((things AS things_9 INNER JOIN is_Url_documento_fonte_of ON things_9.[id thing] = is_Url_documento_fonte_of.soggetto) INNER JOIN ((things AS things_10 INNER JOIN is_Host_documento_fonte_of ON things_10.[id thing] = is_Host_documento_fonte_of.soggetto) INNER JOIN ((things AS things_8 INNER JOIN is_autore_documento_of ON things_8.[id thing] = is_autore_documento_of.soggetto) INNER JOIN ((things INNER JOIN is_Ambito_riferimento_of ON things.[id thing] = is_Ambito_riferimento_of.soggetto) INNER JOIN ((((things AS things_4 INNER JOIN ((is_lemma_of INNER JOIN things AS things_3 ON is_lemma_of.oggetto = things_3.[id thing]) INNER JOIN is_autore_definizione_of ON things_3.[id thing] = is_autore_definizione_of.oggetto) ON things_4.[id thing] = is_autore_definizione_of.soggetto) INNER JOIN (things AS things_6 INNER JOIN is_url_definizione_of ON things_6.[id thing] = is_url_definizione_of.soggetto) ON things_3.[id thing] = is_url_definizione_of.oggetto) INNER JOIN (things AS things_5 INNER JOIN is_posizione_definizione_of ON things_5.[id thing] = is_posizione_definizione_of.soggetto) ON things_3.[id thing] = is_posizione_definizione_of.oggetto) INNER JOIN (is_titolo_documento_of INNER JOIN things AS things_7 ON is_titolo_documento_of.soggetto = things_7.[id thing]) ON things_3.[id thing] = is_titolo_documento_of.oggetto) ON is_Ambito_riferimento_of.oggetto = things_3.[id thing]) ON is_autore_documento_of.oggetto = things_7.[id thing]) ON is_Host_documento_fonte_of.oggetto = things_7.[id thing]) ON is_Url_documento_fonte_of.oggetto = things_7.[id thing]) ON things_1.[id thing] = is_lemma_of.soggetto) INNER JOIN (things AS things_2 INNER JOIN is_Acronimo_of ON things_2.[id thing] = is_Acronimo_of.soggetto) ON things_1.[id thing] = is_Acronimo_of.oggetto ORDER BY things_1.thing;"

class QueryFormName(forms.Form):
    SQL_query = forms.CharField(widget=forms.Textarea, initial=Query_initial_string, label="") #type your default query here
    # la label="" come input è per evitare che nel form compaia automaticamente "sql query"



