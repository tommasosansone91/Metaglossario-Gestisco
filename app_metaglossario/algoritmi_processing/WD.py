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

    # devo importare non elab1 ma le tabelle relazionali

    

    saving_folder_name = 'saved_dataframes'
    ER_folder_name = 'tabelle_entita_e_relazionali'
    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    folder_Elab_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name)
    folder_ER_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+ER_folder_name)


    nomi_Tabelle_relazionali = ["is_Acronimo_of", "is_Lemma_of", "is_Ambito_riferimento_of", "is_Autore_definizione_of", "is_Posizione_definizione_of", "is_Url_definizione_of", "is_Titolo_documento_fonte_of", "is_Autore_documento_fonte_of", "is_Host_documento_fonte_of", "is_Url_documento_fonte_of", "is_Commento_entry_of", "is_Data_inserimento_entry_of", "is_Id_statico_entry_of", "is_Admin_approval_switch_of"]

    Things = pd.read_excel(folder_ER_dir+r'\\Things.xlsx', head=True, index_col=0)

    is_Acronimo_of = pd.read_excel(folder_ER_dir+r'\\is_Acronimo_of.xlsx', head=True, index_col=0)
    is_Lemma_of = pd.read_excel(folder_ER_dir+r'\\is_Lemma_of.xlsx', head=True, index_col=0)
    is_Ambito_riferimento_of = pd.read_excel(folder_ER_dir+r'\\is_Ambito_riferimento_of.xlsx', head=True, index_col=0)
    is_Autore_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Autore_definizione_of.xlsx', head=True, index_col=0)
    is_Posizione_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Posizione_definizione_of.xlsx', head=True, index_col=0)
    is_Url_definizione_of = pd.read_excel(folder_ER_dir+r'\\is_Url_definizione_of.xlsx', head=True, index_col=0)
    is_Titolo_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Titolo_documento_fonte_of.xlsx', head=True, index_col=0)
    is_Autore_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Autore_documento_fonte_of.xlsx', head=True, index_col=0)
    is_Host_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Host_documento_fonte_of.xlsx', head=True, index_col=0)
    is_Url_documento_fonte_of = pd.read_excel(folder_ER_dir+r'\\is_Url_documento_fonte_of.xlsx', head=True, index_col=0)
    is_Commento_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Commento_entry_of.xlsx', head=True, index_col=0)
    is_Data_inserimento_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Data_inserimento_entry_of.xlsx', head=True, index_col=0)
    is_Id_statico_entry_of = pd.read_excel(folder_ER_dir+r'\\is_Id_statico_entry_of.xlsx', head=True, index_col=0)
    is_Admin_approval_switch_of = pd.read_excel(folder_ER_dir+r'\\is_Admin_approval_switch_of.xlsx', head=True, index_col=0)


    Tabelle_relazionali = [is_Acronimo_of, is_Lemma_of, is_Ambito_riferimento_of, is_Autore_definizione_of, is_Posizione_definizione_of, is_Url_definizione_of, is_Titolo_documento_fonte_of, is_Autore_documento_fonte_of, is_Host_documento_fonte_of, is_Url_documento_fonte_of, is_Commento_entry_of, is_Data_inserimento_entry_of, is_Id_statico_entry_of, is_Admin_approval_switch_of]


    nC = len(Tabelle_relazionali)

    print("Vengono importate le tabelle delle entità e relazionali dalla directory %s ..." % folder_ER_dir)

    print("Things")
    print(Things)
    print("--------------------------------")

    for k in range(nC):

        print(nomi_Tabelle_relazionali[k])
        print(Tabelle_relazionali[k])
        print("--------------------------------")


    ##################################################
    ##################################################
    ##################################################
    ##################################################
    ##################################################
    ##################################################
    ##################################################

    # usala per riempire il modello node, seguendo la struttura relazionale del metaglossario
    # aggiungi commento entri e admin approval switch


    #setta la dimensione dell'ID    
    ID_dimension = 1000000
    


    print("*****************************************")

    model_node.objects.all().delete()
    print("Eliminati tutti i dati dentro model_node!")

    print("Il modello nodale viene riempito coi dati della tabella Things sulla base dei dati contenuti nelle tabelle relazionali...")


    # Per ogni entità, compila il modello nodale

    # ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "
    # Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", 
    # "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]
    
        

    Things = Things.sort_values(["ID_db_Thing", "Thing"])
    Things = Things.reset_index(drop=True)

    is_Id_statico_entry_of = is_Id_statico_entry_of.sort_values(["ID_db_Id_statico_entry", "ID_db_Thing"])
    is_Id_statico_entry_of = is_Id_statico_entry_of.reset_index(drop=True)

    ###################################################
     # ambito riferimento -- definizioni, id statico,
    ##################################################

    is_Ambito_riferimento_of = is_Ambito_riferimento_of.sort_values(["ID_db_Ambito_riferimento", "ID_db_Definizione"])
    is_Ambito_riferimento_of = is_Ambito_riferimento_of.reset_index(drop=True)

    # for i in is_Ambito_riferimento_of



    
    



    




  





