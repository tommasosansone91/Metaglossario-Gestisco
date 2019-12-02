from app_metaglossario.entity_relationship_models import *
from app_metaglossario.node_models import *
from app_metaglossario.models import displaying_terminology


def algoritmo_WD():

    print("Viene richiamato l'algoritmo WD!")

    # algoritmo per organizzare i dati per la visualizzazione
    # la chiave è costruire una vista che permette di vedere un oggetto alla volta, 
    # col punto di vista incentrato su quell'oggetto, circondato dai related.

    # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

    import numpy as np
    import pandas as pd

    # importa la tabella excel Elab 1 e salvala come dataframe

    import os    
    from django.contrib.staticfiles import finders

    saving_file_name = 'Elab1.xlsx'

    saving_folder_name = 'saved_dataframes'

    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)

    Elab1 = pd.read_excel(df_dir, head=True, index_col=0)

    

    print("Viene importato il dataframe Elab1 dalla directory %s !" % df_dir)

    print(Elab1)

    

    # usala per riempire il modello node, seguendo la struttura relazionale del metaglossario
    # aggiungi commento entri e admin approval switch

    L_GI = len(Elab1.index)
    nC = len(Elab1.columns)
    
    #il risultato di questa operazione è automaticamente un float!
    # metto int dentro try per correggerlo


    if (nC % 2) != 0:
        raise ValueError("ERRORE! Il file in ingresso Elab1 deve necessariamente avere un numero di colonne pari, perchè formato da ID_db ed entità corrispondenti!")

    
    nC = int(nC/2)

    print("Dimensioni del dataframe:")
    print("Righe (L_GI): %s" % L_GI)
    print("Colonne (nC): %s" % nC)  

    # salvo i nomi delle colonne
    label_Elab1 = list(Elab1.columns)

    #setta la dimensione dell'ID    
    ID_dimension = 1000000

    print("*****************************************")

    model_node.objects.all().delete()
    print("Eliminati tutti i dati dentro model_node!")

    print("Il modello nodale viene riempito sulla base dei dati contenuti in Elab1...")


    # Per ogni entità, compila il modello nodale

    # ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "
    # Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", 
    # "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]
    
    # Lemma -- acronimi, id statico,     

    Elab1 = Elab1.sort_values(["Lemma", "Id_statico_entry"])
    Elab1 = Elab1.reset_index(drop=True)
    



    




  





