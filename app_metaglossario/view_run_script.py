from django.shortcuts import render, redirect
import time


# per gli script di calcolo tempo degli algoritmi
# per gli script di elaborazione della terminologia
from .algoritmi_processing import *

# per gli script ausiliari
from .algoritmi_processing.script_ausiliari import *

# per gli script di management delle entry singole
from .algoritmi_processing.gestione_modello_entry import *

# per gli script di management dei file glossario
from .algoritmi_processing.gestione_modello_file import *

# per gli script di svuotamento dei modelli
from .algoritmi_processing.svuotamento_modelli import *

# per l'aloritmo di preparazione del glossario di ingresso
from .algoritmi_processing.PGI import *

# per l'algoritmo di identificazione della terminologia
from .algoritmi_processing.SR_ridotto import *






def run_script(request):   

    print("***************************************")
    print("*** Script richiamato con successo! ***")

    start_time = time.time()  
    
    erase_acquired_terminology()

    pour_entire_entry_model()
    pour_entire_file_model()

    erase_prepared_terminology()    
    
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