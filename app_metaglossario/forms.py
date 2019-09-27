from django import forms
from .models import glossary_entry


class glossary_entry_form(forms.ModelForm):
        
        
        
    class Meta:
        model=glossary_entry
        fields=["Lemma_it", "Lemma_ch", "Acronimo_it", "Acronimo_ch", "Definizione_it", "Definizione_ch", "Ambito_riferimento_it", "Ambito_riferimento_ch", "Autore_definizione_it", "Autore_definizione_ch", "Posizione_definizione_it", "Posizione_definizione_ch", "Url_definizione_it", "Url_definizione_ch", "Titolo_documento_fonte_it", "Titolo_documento_fonte_ch", "Autore_documento_fonte_it", "Autore_documento_fonte_ch", "Host_documento_fonte_it", "Host_documento_fonte_ch", "Url_documento_fonte_it", "Url_documento_fonte_ch", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]

