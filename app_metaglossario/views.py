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
from .algoritmi_processing.script_gestione import *

# per gli script di calcolo tempo degli algoritmi
from .algoritmi_processing.script_ausiliari import *

# per gli script di elaborazione della terminologia
from .algoritmi_processing.PGI import algoritmo_PGI
from .algoritmi_processing.SR import algoritmo_SR
from .algoritmi_processing.WD import algoritmo_WD


# per il query wizard
from .forms import QueryFormName



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


def glossario(request):   

    query = request.GET.get('q') #q è variabile risultante dalla query del database
    # non sostuituirla col valore vuoto

    template = "glossario.html" #il template è sempre lo stesso

    all_entries = prepared_terminology.objects.all() #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)

    # se la query è stata fatta
    if query:

        query = request.GET.get('q') #q è variabile risultante dalla query del database

        selected_entries = prepared_terminology.objects.filter(Q(Acronimo__icontains=query)|Q(Ambito_riferimento__icontains=query)|Q(Autore_definizione__icontains=query)|Q(Autore_documento_fonte__icontains=query)|Q(Data_inserimento_entry__icontains=query)|Q(Definizione__icontains=query)|Q(Host_documento_fonte__icontains=query)|Q(Id_statico_entry__icontains=query)|Q(Lemma__icontains=query)|Q(Posizione_definizione__icontains=query)|Q(Titolo_documento_fonte__icontains=query)|Q(Url_definizione__icontains=query)|Q(Url_documento_fonte__icontains=query))
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

def pagina_api(request):
    return render(request, 'api.html', {})


def query_wizard(request):
    
    # from app_metaglossario import forms
    # from forms import QueryFormName

    QWform = QueryFormName()



    if request.method == 'POST': #se qualcuno clicca su "submit", cioè esegue una post
        QWform = QueryFormName(request.POST)

        if QWform.is_valid(): #validation check
            
            print("Query SQL acquisita:"+ QWform.cleaned_data['SQL_query'])
            #esempio SELECT * FROM things2 WHERE ID_Things <1000021

            # agisci qui

            import psycopg2 as pg2

            mydb = pg2.connect(user='zogpunyhfdizcj', password='e4e8bbb8ef02572179d0ccdc1a146d4f2eba03e587525349bb4436a80b87f4ec',
                                          host='ec2-46-51-190-87.eu-west-1.compute.amazonaws.com', database='dfibp7p1uu70v7')

            #'postgres://zogpunyhfdizcj:e4e8bbb8ef02572179d0ccdc1a146d4f2eba03e587525349bb4436a80b87f4ec@ec2-46-51-190-87.eu-west-1.compute.amazonaws.com:5432/dfibp7p1uu70v7')
            #postgres://user:password@host:porta/database_name

            # import mysql.connector

            # # connect to the database
            # mydb = mysql.connector.connect(user='root', password='metaglossariov2',
            #                               host='localhost', database='schema_meta_prova')


            

            my_cursor = mydb.cursor()
            my_cursor.execute(QWform.cleaned_data['SQL_query'])

            query_result_list = my_cursor.fetchall()

            len_result_list = len(query_result_list)
           
            #Parla alla console
            print("Query eseguita sul database con successo, risultati inviati al browser!")

            # print("************************************")
            # print("Risutati della query:")

            # so che mi ritorna una lista di tuple: allora mi preparo a stampare con un doppio ciclo for a mo' di matrice
            # for record in query_result_list:
            #     for entity in record:
            #         print(entity)
            #     print("---")

            print("************************************")

            #devo creare una matrice
            context_diz={'QWform':QWform, 'queryresult_key' :query_result_list, 'len_result_list_key':len_result_list}
            # non ho una views che ne crea il dizionario della chiave e della lista
            # faccio una vista che mi ritorna entrambe le cose con un dzionario a due elementi

    else:
        context_diz={'QWform':QWform}

    return render(request,'query_wizard.html',context_diz)



# def vista_ricerca_semplice(request):

#     template = "glossario.html"

#     query = request.GET.get('q') #q è variabile risultante dalla query del database

#     selected_entries = glossary_entry.objects.filter(Q(Lemma_it__icontains=query))

#     context = {'selected_entries':selected_entries}

#     #return render(request, template, context)
#     return render(request, 'glossario.html', {'selected_entries':selected_entries})









