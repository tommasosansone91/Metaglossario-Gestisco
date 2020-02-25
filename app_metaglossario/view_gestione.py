from django.shortcuts import render, redirect
import time


# meglio non usare la tipologia di importazione wildcard

# per gli script di elaborazione della terminologia
from .algoritmi_processing import script_ausiliari
from .algoritmi_processing import svuotamento_modelli
from .algoritmi_processing import gestione_modello_entry
from .algoritmi_processing import gestione_modello_file
from .algoritmi_processing import PGI
from .algoritmi_processing import SR_ridotto

# per gli script ausiliari
from .algoritmi_processing.script_ausiliari import *

# per gli script di management delle entry singole
from .algoritmi_processing.gestione_modello_entry import pour_latest_entry
from .algoritmi_processing.gestione_modello_entry import pour_entire_entry_model

# per gli script di management dei file glossario
from .algoritmi_processing.gestione_modello_file import pour_latest_file
from .algoritmi_processing.gestione_modello_file import pour_entire_file_model

# per gli script di svuotamento dei modelli
from .algoritmi_processing.svuotamento_modelli import erase_acquired_terminology
from .algoritmi_processing.svuotamento_modelli import erase_prepared_terminology

# per l'aloritmo di preparazione del glossario di ingresso
from .algoritmi_processing.PGI import algoritmo_PGI

# per l'algoritmo di identificazione della terminologia
from .algoritmi_processing.SR_ridotto import algoritmo_SR_ridotto

# login required per abilitare accesso e run solo agli amministratori
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# per le funzioni che permettono di ottenere il nome della funzione
import inspect



# funzione vista
# ci può accedere solo chi è admin
@staff_member_required
def istruzioni_gestione_terminologia(request):
    return render(request, 'gestione/istruzioni_gestione_terminologia.html', {})


# funzione vista
# ci può accedere solo chi è admin
@staff_member_required
def tutorial_admin(request):
    return render(request, 'gestione/tutorial_admin.html', {})


# funzione vista
# ci può accedere solo chi è admin
@login_required
def tutorial_utenti(request):
    return render(request, 'tutorial_utenti.html', {})

# funzione vista
# ci può accedere solo chi è admin
@staff_member_required
def pannello_gestione_terminologia(request):

    
    # se ho ricevuto il click del pulsante nel form, con valore run_script
    if request.method == 'POST':
        

        # call function

        print("***************************************")
        print("*** Script richiamato con successo! ***")
        print("***************************************")

        print("Viene lanciato lo script:")

        start_time = time.time()

        # scelta della funzione

        if 'script_1' in request.POST:
            script_return_dict = Riversamento_standard()
        
        if 'script_2' in request.POST:
            script_return_dict = Riversamento_cumulativo_completo()

        if 'script_3' in request.POST:
            script_return_dict = Resetta_database_output()

        if 'script_4' in request.POST:
            script_return_dict = Riversamento_cumulativo_tuple()

        if 'script_5' in request.POST:
            script_return_dict = Riversamento_cumulativo_file()





        end_time = time.time()

        elapsed_time = round(end_time - start_time)

        start_time = time.ctime(start_time)
        end_time = time.ctime(end_time)

        print("***************************************")
        print("*** Script eseguito fino alla fine! ***")
        print("*** Tempo impiegato: %s s ***" % elapsed_time )
        print("***************************************")

        context_dict = {'script_is_run':'yes', 'tempo_inizio':start_time, 'tempo_fine':end_time, 'tempo_impiegato':elapsed_time}

        context_dict.update(script_return_dict)

        

        # return user to required page
        # return HttpResponseRedirect(reverse('management_keyboard'))
        return render(request, 'gestione/pannello_gestione_terminologia.html', context_dict)

    else:
        context_dict = {}
        

    return render(request, 'gestione/pannello_gestione_terminologia.html', context_dict)



##########################################################################################################
# elenco degli script disponibili

# funzione che viene richiamata dall funzione vista
def Riversamento_standard():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")
   
    
    erase_acquired_terminology()

    pour_entire_entry_model()
    pour_entire_file_model()

    erase_prepared_terminology()    
    
    algoritmo_PGI()
    algoritmo_SR_ridotto()

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)


def Riversamento_cumulativo_completo():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")
    
    # non richiamato erase_acquired_terminology()

    pour_entire_entry_model()
    pour_entire_file_model()

    erase_prepared_terminology()    
    
    algoritmo_PGI()
    algoritmo_SR_ridotto()

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)


def Riversamento_cumulativo_tuple():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")
    
    pour_entire_entry_model()
    
    erase_prepared_terminology()    
    
    algoritmo_PGI()
    algoritmo_SR_ridotto()

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)



def Riversamento_cumulativo_file():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")

    pour_entire_file_model()

    erase_prepared_terminology()    
    
    algoritmo_PGI()
    algoritmo_SR_ridotto()

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)



def Resetta_database_output():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")
    
    erase_acquired_terminology()
    erase_prepared_terminology()      

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)



def script_4():  
    
    script_name = inspect.currentframe().f_code.co_name
    print (script_name)
    print("***************************************")
   
    
    # erase_acquired_terminology()

    # pour_entire_entry_model()
    # pour_entire_file_model()

    # erase_prepared_terminology()    
    
    # algoritmo_PGI()
    # algoritmo_SR_ridotto()

    script_return_dict = {'script_name':script_name}

    return(script_return_dict)


