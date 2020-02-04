from django import forms
from .models import glossary_entry
from .models import glossary_file


class glossary_entry_form(forms.ModelForm):
                
    class Meta:
        model = glossary_entry
        fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]


class glossary_file_form(forms.ModelForm):

    class Meta:
        model = glossary_file
        fields = ["Glossary_file", "Data_inserimento_glossary"]






