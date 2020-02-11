from django import forms
from .models import glossary_entry
from .models import glossary_file

# per la gestione dei dati utente
from django.contrib.auth.models import User
from .models_users_authentication import UserProfileInfo



class glossary_entry_form(forms.ModelForm):
                
    class Meta:
        model = glossary_entry
        fields = ["Lemma_it", "Acronimo_it", "Definizione_it", "Ambito_riferimento_it", "Autore_definizione_it", "Posizione_definizione_it", "Url_definizione_it", "Titolo_documento_fonte_it", "Autore_documento_fonte_it", "Host_documento_fonte_it", "Url_documento_fonte_it", "Lemma_ch", "Acronimo_ch", "Definizione_ch", "Ambito_riferimento_ch", "Autore_definizione_ch", "Posizione_definizione_ch", "Url_definizione_ch", "Titolo_documento_fonte_ch", "Autore_documento_fonte_ch", "Host_documento_fonte_ch", "Url_documento_fonte_ch", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]


class glossary_file_form(forms.ModelForm):

    class Meta:
        model = glossary_file
        fields = ["Glossary_file", "Data_inserimento_glossary"]


# form delle info utente
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User 
        # è il modello preimpostato di Django
        fields = ['username', 'email', 'password'] 


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        # è il modello aggiunto da me
        fields = ["profile_pic", "user_link" ]
        


