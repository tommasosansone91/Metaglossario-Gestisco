from django.shortcuts import render, redirect

from .models import glossary_entry
from .forms import glossary_entry_form

from .models import glossary_file
from .forms import glossary_file_form

from .models import acquired_terminology

# from .forms import glossary_sheet_form

# questo mi consente di lanciare i messaggi da una pagina all'altra
from django.contrib import messages

# per la ricerca
from django.db.models import Q

# per la paginazione
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

# per creare api e consentire di esportarle
from django.http import JsonResponse


# per i messaggi a capo
# from django.utils.safestring import mark_safe

# per caricare i files dagli utenti
from django.core.files.storage import FileSystemStorage

# per gli script di management dei files
from .scripts import printout, printout_input
from .scripts import pour_entire_simple_model, pour_entire_file_model
from .scripts import pour_latest_file, pour_latest_entry
from .scripts import erase_acquired_terminology, erase_glossary_entry

# Create your views here.
def home(request):
    return render(request, 'home.html', {})



def glossario(request):

    

    query = request.GET.get('q') #q è variabile risultante dalla query del database
    # non sostuituirla col valore vuoto

    template = "glossario.html" #il template è sempre lo stesso

    all_entries = acquired_terminology.objects.all() #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)

    # se la query è stata fatta
    if query:

        query = request.GET.get('q') #q è variabile risultante dalla query del database

        selected_entries = acquired_terminology.objects.filter(Q(Acronimo__icontains=query)|Q(Ambito_riferimento__icontains=query)|Q(Autore_definizione__icontains=query)|Q(Autore_documento_fonte__icontains=query)|Q(Data_inserimento_entry__icontains=query)|Q(Definizione__icontains=query)|Q(Host_documento_fonte__icontains=query)|Q(Id_statico_entry__icontains=query)|Q(Lemma__icontains=query)|Q(Posizione_definizione__icontains=query)|Q(Titolo_documento_fonte__icontains=query)|Q(Url_definizione__icontains=query)|Q(Url_documento_fonte__icontains=query))
        # Q(Acronimo__icontains=query dice quali sono i campi in cui cercare l'input specificato dall'utente

        # Pagination
        paginator = Paginator(selected_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        selected_entries = paginator.get_page(page)

        # context = {'all_entries':selected_entries}
        #return render(request, template, context)
        # {'nome della variabile con cui sarà richiamato nel template':contenuto}
        return render(request, template, {'all_entries':selected_entries, 'query':query})

    # se non è stata fatta nessuna query
    else:

        # Pagination
        paginator = Paginator(all_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        all_entries = paginator.get_page(page)

        return render(request, template, {'all_entries':all_entries, 'query':query})


# QUESTA è LA SINGOLA ENTRY
def aggiungi_terminologia(request):

    # erase_glossary_entry()
    # erase_acquired_terminology()
    # pour_entire_simple_model()
    # pour_entire_file_model()
    # pour_latest_file()

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

    all_entries = glossary_entry.objects.all() #[:30] #tutti fino al 30simo

    data = {"entries":list(all_entries.values("Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry"))}

    response= JsonResponse(data)
    return response
    # qui manca il passaggio del template, ma forseva bene così

def pagina_api(request):
    return render(request, 'api.html', {})



# def vista_ricerca_semplice(request):

#     template = "glossario.html"

#     query = request.GET.get('q') #q è variabile risultante dalla query del database

#     selected_entries = glossary_entry.objects.filter(Q(Lemma_it__icontains=query))

#     context = {'selected_entries':selected_entries}

#     #return render(request, template, context)
#     return render(request, 'glossario.html', {'selected_entries':selected_entries})
