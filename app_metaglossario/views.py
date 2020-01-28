from django.shortcuts import render, redirect

from .models import glossary_entry
from .forms import glossary_entry_form

from .models import glossary_file
from .forms import glossary_file_form

from .models import acquired_terminology
from .models import prepared_terminology

# from .forms import glossary_sheet_form

# questo mi consente di lanciare i messaggi da una pagina all'altra
from django.contrib import messages

# per creare api e consentire di esportarle
from django.http import JsonResponse


# per i messaggi a capo
# from django.utils.safestring import mark_safe

# per caricare i files dagli utenti
from django.core.files.storage import FileSystemStorage

# per gli script di management dei files
from .algoritmi_processing.script_gestione import *

# per gli script di calcolo tempo degli algoritmi
from .algoritmi_processing.script_ausiliari import *

# per gli script di elaborazione della terminologia
from .algoritmi_processing.PGI import algoritmo_PGI
from .algoritmi_processing.SR import algoritmo_SR
from .algoritmi_processing.WD import algoritmo_WD


# per il query wizard
import pandas as pd
import numpy as np


def run_script(request):   

    start_time = printout()
    # erase_glossary_entry()
    # erase_acquired_terminology()
    # pour_entire_simple_model()
    # pour_entire_file_model()
    # pour_latest_file()
    
    # algoritmo_PGI()
    algoritmo_SR()
    # algoritmo_WD()

    # erase_database_tables()

    import time
    elapsed_time = round(time.time() - start_time)

    print("*** Script eseguito fino alla fine! ***")
    print("*** Tempo impiegato: %s s ***" % elapsed_time )

    finish_sound()

    return render(request, 'run_script.html', {})





# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def indice_glossario(request):   

    template = "indice_glossario.html" #il template è sempre lo stesso
    all_entries = prepared_terminology.objects.all() #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)

    return render(request, template, {'all_entries':all_entries})



# QUESTA è LA SINGOLA ENTRY
def aggiungi_terminologia(request):

    #se si esegue il POST (click del pulsante submit)
    if request.method=='POST':
        form = glossary_entry_form(request.POST or None)

        # request.POST è il contenuto inserito dagli utenti perchè request è il paramentro in ingresso della funzione

        if form.is_valid(): # funzione che controlla la coerenza dei campi (mail, url, numerico, testo, ecc.)
            form.save()
            insert_attempt_output="corretto"
            # insert_attempt_output formatta il colore del messaggio, vedi in base.html
            messages.success(request, ("Terminologia inserita con successo!\nAttendere la convalida da parte dell\'amministratore.\n Per favore non inserire di nuovo la stessa terminologia"))
            
            # per ora non lo uso
            # pour_latest_entry()

            return redirect('aggiungi_terminologia')
            # con redirect non posso usare .html, ma per forza names

        else:
            insert_attempt_output="errato"
            messages.error(request, ('ERRORE: La terminologia non è stata inserita nel glossario.\nCompilare almeno un campo e la data di inserimento.'))
            return render(request, 'aggiungi_terminologia.html', {'insert_attempt_output':insert_attempt_output})

    # se si va sulla pagina e basta
    else:
        return render(request, 'aggiungi_terminologia.html', {})



# per aggiungere la terminologia in massa
def aggiungi_glossario(request):

    #se si esegue il POST (click del pulsante submit)
    if request.method=='POST':

        form = glossary_file_form(request.POST, request.FILES)
        # form = glossary_file_form(request.POST, request.FILES)
        # funziona anche con
        # form = glossary_file_form(request.POST or None, request.FILES or None)

        if form.is_valid():
            form.save()
            insert_attempt_output="corretto"
            # insert_attempt_output formatta il colore del messaggio, vedi in base.html
            messages.success(request, ("Glossario inserito con successo!\nAttendere la convalida da parte dell\'amministratore.\n Per favore non inserire di nuovo la stessa terminologia"))
            
            #  per ora non lo uso
            # pour_latest_file()

            return redirect('aggiungi_glossario')

        else:
            insert_attempt_output="errato"
            messages.error(request, ('ERRORE: Non è stato caricato alcun glossario.'))
            return render(request, 'aggiungi_glossario.html', {'insert_attempt_output':insert_attempt_output})

    # se si va sulla pagina e basta
    else:
        return render(request, 'aggiungi_glossario.html', {})


# per esportare il contenuto glossario tramite API
def api_glossario(request):

    all_entries = prepared_terminology.objects.all() #[:30] #tutti fino al 30simo

    data = {"entries":list(all_entries.values("Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry"))}

    response= JsonResponse(data)
    return response
    # qui manca il passaggio del template, ma forseva bene così
    # questo template non viene usato


def esporta_terminologia(request):
    return render(request, 'esporta_terminologia.html', {})


# info pages section
def che_cos_e_un_metaglossario(request):
    return render(request, 'info/che_cos_e_un_metaglossario.html', {})

def codice_sorgente(request):
    return render(request, 'info/codice_sorgente.html', {})

def come_sono_organizzati_i_dati(request):
    return render(request, 'info/che_cos_e_un_metaglossario.html', {})

def istruzioni_per_l_uso(request):
    return render(request, 'info/istruzioni_per_l_uso.html', {})

def bibliografia(request):
    return render(request, 'info/bibliografia.html', {})

def perche_un_metaglossario(request):
    return render(request, 'info/perche_un_metaglossario.html', {})

def ringraziamenti(request):
    return render(request, 'info/ringraziamenti.html', {})

# ----------


