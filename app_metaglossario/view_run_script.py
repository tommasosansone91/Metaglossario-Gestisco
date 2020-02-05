from django.shortcuts import render, redirect
import time

# per gli script di management dei files
from .algoritmi_processing.script_gestione import *

# per gli script di calcolo tempo degli algoritmi
from .algoritmi_processing.script_ausiliari import *

# per gli script di elaborazione della terminologia
from .algoritmi_processing.PGI import algoritmo_PGI
from .algoritmi_processing.SR_ridotto import algoritmo_SR_ridotto

# from .algoritmi_processing.WD import algoritmo_WD


def run_script(request):   

    print("***************************************")
    print("*** Script richiamato con successo! ***")

    start_time = time.time()  
    
    erase_acquired_terminology()

    pour_entire_entry_model()
    # pour_entire_file_model()
    
    
    algoritmo_PGI()
    algoritmo_SR_ridotto()
    

    
    elapsed_time = round(time.time() - start_time)

    print("***************************************")
    print("*** Script eseguito fino alla fine! ***")
    print("*** Tempo impiegato: %s s ***" % elapsed_time )
    print("***************************************")

    finish_sound()
    # no, il suono va fatto lanciare nel template

    return render(request, 'run_script.html', {})