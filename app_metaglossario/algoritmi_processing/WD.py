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




    # ora genero anche le tabelle ISIO separate pr entità

    print("Vengono generate le tabelle ISIO: is_static_id_of + nomi entità, per l'algoritmo WD...")

    # per generarle devo importare elab1
    saving_file_name = 'Elab1.xlsx'

    saving_folder_name = 'saved_dataframes'

    finders.find(saving_folder_name)
    searched_locations = finders.searched_locations
    df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)

    Elab1 = pd.read_excel(df_dir, head=True, index_col=0)    

    print("Viene importato il dataframe Elab1 dalla directory %s !" % df_dir)

    print(Elab1)    

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

    ISIO_Lemma = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Definizione"], Elab1["Id_statico_entry"], Elab1["Definizione"] ], axis=1) # è dataframe
    ISIO_Acronimo = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Acronimo"], Elab1["Id_statico_entry"], Elab1["Acronimo"] ], axis=1) 
    ISIO_Definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Definizione"], Elab1["Id_statico_entry"], Elab1["Definizione"] ], axis=1) 
    ISIO_Ambito_riferimento = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Ambito_riferimento"], Elab1["Id_statico_entry"], Elab1["Ambito_riferimento"] ], axis=1)
    ISIO_Autore_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Autore_definizione"], Elab1["Id_statico_entry"], Elab1["Autore_definizione"] ], axis=1) 
    ISIO_Posizione_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Posizione_definizione"], Elab1["Id_statico_entry"], Elab1["Posizione_definizione"] ], axis=1) 
    ISIO_Url_definizione = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Url_definizione"], Elab1["Id_statico_entry"], Elab1["Url_definizione"] ], axis=1)  
    ISIO_Titolo_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Titolo_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Titolo_documento_fonte"] ], axis=1) 
    ISIO_Autore_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Autore_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Autore_documento_fonte"] ], axis=1) 
    ISIO_Host_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Host_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Host_documento_fonte"] ], axis=1) 
    ISIO_Url_documento_fonte = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Url_documento_fonte"], Elab1["Id_statico_entry"], Elab1["Url_documento_fonte"] ], axis=1) 
    ISIO_Commento_entry = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Commento_entry"], Elab1["Id_statico_entry"], Elab1["Commento_entry"] ], axis=1) 
    ISIO_Data_inserimento_entry = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Data_inserimento_entry"], Elab1["Id_statico_entry"], Elab1["Data_inserimento_entry"] ], axis=1) 
    ISIO_Admin_approval_switch = pd.concat( [ Elab1["ID_db_Id_statico_entry"], Elab1["ID_db_Admin_approval_switch"], Elab1["Id_statico_entry"], Elab1["Admin_approval_switch"] ], axis=1) 



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
    ###################################################

    is_Ambito_riferimento_of = is_Ambito_riferimento_of.sort_values(["ID_db_Ambito_riferimento", "ID_db_Definizione"])
    is_Ambito_riferimento_of = is_Ambito_riferimento_of.reset_index(drop=True)


    for i in range(len(is_Ambito_riferimento_of)):

        # creo il nodo
        current_node = model_node.objects.create()
        
        current_node.centered_ID = is_Ambito_riferimento_of.iloc[i, 0] 
        current_node.centered_Thing = is_Ambito_riferimento_of.iloc[i, 1] 
        current_node.entita = "Ambito_riferimento"

        
        # scrivi le definizioni
        lista_connected_Definizione_ID = []
        lista_connected_Definizione = []

        # scrivi subito la prima definizione
        lista_connected_Definizione_ID = lista_connected_Definizione_ID.append(is_Ambito_riferimento_of.iloc[i, 2])
        lista_connected_Definizione = lista_connected_Definizione.append(is_Ambito_riferimento_of.iloc[i, 3])

        c_rip=0

        #ciclo while delle definizioni
        while is_Ambito_riferimento_of.iloc[i, 0] == is_Ambito_riferimento_of.iloc[i+1, 0]: # uguaglianza id cs

            if is_Ambito_riferimento_of.iloc[i, 1] != is_Ambito_riferimento_of.iloc[i+1, 1] and c_rip>0: # uguaglianza id acronimi

                lista_connected_Definizione_ID = lista_connected_Definizione_ID.append(is_Ambito_riferimento_of.iloc[i, 2])
                lista_connected_Definizione = lista_connected_Definizione.append(is_Ambito_riferimento_of.iloc[i, 3])

            c_rip = c_rip + 1

            # forza la scrittura dell'ultima definizione
            if is_Ambito_riferimento_of.iloc[i, 1] != is_Ambito_riferimento_of.iloc[i+1, 1] and c_rip>0: # uguaglianza id acronimi

                lista_connected_Definizione_ID = lista_connected_Definizione_ID.append(is_Ambito_riferimento_of.iloc[i, 2])
                lista_connected_Definizione = lista_connected_Definizione.append(is_Ambito_riferimento_of.iloc[i, 3])
    
            # fine della scrittura delle definizioni

            # scrivi gli id statici
            lista_connected_Id_statico_entry_ID = []
            lista_connected_Id_statico_entry = []

             # scrivi subito il primo ID statico
            lista_connected_Id_statico_entry_ID = lista_connected_Id_statico_entry_ID.append(ISIO_Ambito_riferimento.iloc[i, 2])
            lista_connected_Id_statico_entry = lista_connected_Id_statico_entry.append(ISIO_Ambito_riferimento.iloc[i, 3])

            # ciclo while dei id statici
            while ISIO_Ambito_riferimento.iloc[i, 0] == ISIO_Ambito_riferimento.iloc[i+1, 0]: # uguaglianza id cs

                if ISIO_Ambito_riferimento.iloc[i, 1] != ISIO_Ambito_riferimento.iloc[i+1, 1] and c_rip>0: # uguaglianza id acronimi

                    lista_connected_Id_statico_entry_ID = lista_connected_Definizione_ID.append(ISIO_Ambito_riferimento.iloc[i, 2])
                    lista_connected_Id_statico_entry = lista_connected_Definizione.append(ISIO_Ambito_riferimento.iloc[i, 3])

            c_rip = c_rip + 1

            # forza la scrittura dell'ultimo id statico
            if ISIO_Ambito_riferimento.iloc[i, 1] != ISIO_Ambito_riferimento.iloc[i+1, 1] and c_rip>0: # uguaglianza id acronimi

                lista_connected_Id_statico_entry_ID = lista_connected_Definizione_ID.append(ISIO_Ambito_riferimento.iloc[i, 2])
                lista_connected_Id_statico_entry = lista_connected_Definizione.append(ISIO_Ambito_riferimento.iloc[i, 3])
    
            # smetto di scrivere gli id statici




  





