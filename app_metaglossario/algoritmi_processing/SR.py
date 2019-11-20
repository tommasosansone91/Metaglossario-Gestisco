def algoritmo_SR():

    # algoritmo per standardizzare i dati prima di incatenarli nella struttura relazionale

    # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

    import numpy as np
    import pandas as pd
    from app_metaglossario.models import prepared_terminology
    from app_metaglossario.models import displaying_terminology
    # from app_metaglossario.metaglossary_models import 

    # devo modificare

    ###############################
    ###  CONTROLLI e PARAMETRI
    ###############################


    #setta la dimensione dell'ID
    
    ID_dimension = 1000000

    print("Inizia la creazione della struttura relazionale dei dati contenuti in prepared_terminology...")
    
    # copia i dati del modello prepared_terminology in un dataframe    

    prepared_entries = prepared_terminology.objects.all()   

    # genera un oggettos trano che contine i nomi delle colonne
    # nomi_campi_prepared_terminology = prepared_terminology._meta.fields

    # devo trovare il modo per farlo in automatico
    # nomi_campi_prepared_terminology = ["Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"]

    # lista coi nomi delle colonne del modello
    nomi_campi_prepared_terminology = [field.name for field in prepared_terminology._meta.get_fields()[1:]]

    # elimino la colonna dell'id stabilito da python
    # nomi_campi_prepared_terminology = nomi_campi_prepared_terminology[1:]

    L_GI = len(prepared_entries)
    nC = len(nomi_campi_prepared_terminology)

    print("Vengono impostate le dimensioni del dataframe:")
    print("Righe (L_GI): %s" % L_GI)
    print("Colonne (nC): %s" % nC)   


    print("Viene generato il dataframe che contiene la copia dei dati del modello prepared_terminology...")

    # creo il dataframe
    GI = pd.DataFrame(columns=nomi_campi_prepared_terminology)

    # print(GI)


    for element in prepared_entries:

        # "Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"
        new_entry = {"Lemma":element.Lemma, "Acronimo":element.Acronimo, "Definizione":element.Definizione, "Ambito_riferimento":element.Ambito_riferimento, "Autore_definizione":element.Autore_definizione, "Posizione_definizione":element.Posizione_definizione, "Url_definizione":element.Url_definizione, "Titolo_documento_fonte":element.Titolo_documento_fonte, "Autore_documento_fonte":element.Autore_documento_fonte, "Host_documento_fonte":element.Host_documento_fonte, "Url_documento_fonte":element.Url_documento_fonte, "Commento_entry":element.Commento_entry, "Data_inserimento_entry":element.Data_inserimento_entry, "Id_statico_entry":element.Id_statico_entry, "Admin_approval_switch":element.Admin_approval_switch}
        
        GI = GI.append(new_entry, ignore_index=True)

  
    GI = GI.sort_values(['Lemma', 'Id_statico_entry'])
    GI = GI.reset_index(drop=True)

    print(GI)



    # preparo il tabellone fatto con le tabelle di ID e campi corrispondenti adiacenti    
    print("Vengono preparati gli ID da associare a ciascun oggetto del metaglossario...")

    label_IDs_prestampa = []

    for i in range(nC):
        label_IDs_prestampa.append("ID_db_" + nomi_campi_prepared_terminology[i])
    
    ID_dimension = 1000000

    IDs_prestampa_content = []

    # mentre per python il primo indice è 0, nella mia riga io ci metto 1
    for i in range(L_GI):        
        IDs_prestampa_content.append([ (ID_dimension * (j+1) ) + (i+1) for j in range(nC) ])
            

    IDs_prestampa = pd.DataFrame(IDs_prestampa_content, columns=label_IDs_prestampa)   



    # devo ordinare dalla A alla Z la tabella della terminolgia
    # poi devo reincollare il vettore di ogni colonna già ordinata dalla A alla Z


    Elab1 = pd.concat([IDs_prestampa, GI], axis=1)

    print("Viene preparata la tabella di ID e terminologia Elab1...")

    print("Gli ID di Elab 1 vengono assegnati in ordine numerico ascendente con l'ordine alfabetico (A->Z) di ogni colonna.")

    


    # vedi i print
    for j in range(nC):

        Elab1 = Elab1.sort_values([nomi_campi_prepared_terminology[j], "Id_statico_entry"])
        Elab1 = Elab1.reset_index(drop=True)
        Elab1.iloc[:, j] = IDs_prestampa.iloc[:, j]   
        


    Elab1 = Elab1.sort_values(['Lemma', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    
    print(Elab1)

    # tengo traccia delle ripetizioni presenti in ogni colonna del dataframe

    # creo le labe per il df ripetizioni
    label_ripetizioni = []

    for i in range(nC):
        label_ripetizioni.append("Ripetizioni_di_" + nomi_campi_prepared_terminology[i])

    # creo i dati per il df ripetizioni
    ripetizioni_content = []
    
    ripetizioni_content.append([ 0 for j in range(nC) ])

    # creo  il df ripetizioni
    ripetizioni = pd.DataFrame(ripetizioni_content, columns=label_ripetizioni)
    

    # inizia la riscrittura degli id per mettere uguali queli che corrispondono ad oggetti uguali

    #ordino il glossario alfabeticamente per X

    # pone uguali id di elementi guuali


    # salto il fatto che id statico non ha ripetizioni perchè c'è l'interruttore di show/hide

    label_Elab1 = nomi_campi_prepared_terminology + label_IDs_prestampa

    print("Inizia lo scansionamento della terminologia e dei metadati per individuare elementi uguali...")
    
    
    # faccio il megaciclo in cui rendo uguagli gli id di oggetti uguali adiacenti (ordiant in ordine alfabetico)
    for j in range(nC):

        Elab1 = Elab1.sort_values([nomi_campi_prepared_terminology[j], "Id_statico_entry"])
        Elab1 = Elab1.reset_index(drop=True)

        # uno in meno perchè devo fare confronto tra i e i+1
        for i in range(L_GI-1):

            # se gli oggetti consecutivi sono uguali
            if Elab1.iloc[i+1, j+nC] == Elab1.iloc[i, j+nC] :

                # poni l'id successivo uguale a quello attuale
                Elab1.iloc[i+1, j] = Elab1.iloc[i, j] 

                ripetizioni.iloc[0, j] = ripetizioni.iloc[0, j] + 1


    Elab1 = Elab1.sort_values(["Lemma", "Id_statico_entry"])
    Elab1 = Elab1.reset_index(drop=True)
 

    print(Elab1)

    # creo un dataframe per gli ogetti univoci (L_GI-ripetizioni)

    label_oggetti_univoci = []

    for j in range(nC):
        label_oggetti_univoci.append("Oggetti_univoci_di_" + nomi_campi_prepared_terminology[j])

    # creo i dati per il df ripetizioni
    oggetti_univoci_content = []
    
    oggetti_univoci_content.append([ L_GI - ripetizioni.iloc[0, j] for j in range(nC) ])   
    

    # creo  il df ripetizioni
    oggetti_univoci = pd.DataFrame(oggetti_univoci_content, columns=label_oggetti_univoci)

    

    print("Il metaglossario Elab1 possiede i seguenti numeri di oggetti univoci:")

    print(np.transpose(oggetti_univoci))


    # Inizia il ciclo di sostituzioni degli ID con ID ordinati in linea con gli ID statici

    #  ossia:
    #  tutte le colonne sono ordinate per ID statici,
    #  un ciclo i scorre le colonne, e:
    #  un ciclo j scorre tutta la colonna, e:
    #  l'ID corrente(j) viene salvato come bersaglio da sostituire
    #  viene generato un ID del tipo x000000[contatore del ciclo j /ossia prestampaIDs(j,i)] e salvato come sostituto
    #  un ciclo k scorre tutta la colonna DALLA CELLA CORRENTE VERSO IL BASSO (onde evitare di sovrascrivere i precedenti) e sostituisce altre celle uguali al bersaglio con il sostuituto


    # col_scan 1 To L_GI, 1 To nC
    # avvenuta_sost  1 To L_GI, 1 To nC

    #  va bene anche df_zeros = df * 0

    avvenuta_sost = pd.DataFrame(0, index=np.arange(len(GI)), columns=label_IDs_prestampa)


    # ordino il glossario alfabeticamente per IDS, una sola volta
    Elab1 = Elab1.sort_values("Id_statico_entry")
    Elab1 = Elab1.reset_index(drop=True)

    # in col scan ci metto gli id di elab1 ordinati per ids
    col_scan = Elab1[label_IDs_prestampa]

    

    pd.options.mode.chained_assignment = None  # default='warn'
    # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

    # in VBA, solo negli offset accade che righe e colonne hanno il sistema ribaltato rispetto a x=0 e coordinate scambiate
    # nelle matrici si ragiona normalmente in (righe, colonne)

    for i in range(nC):
    # ciclo delle colonne
    # per l'ID statico non devo farlo ... ma non è più in ultima poizione

        for j in range(L_GI):
        #ciclo delle righe

            Bersaglio = col_scan.iloc[j, i]
            Sostituto = IDs_prestampa.iloc[j, i] # questi sono gli id 1000001 , 10000002, ecc

            

            for k in range(j, L_GI): #[j, j+1,...,L_GI-1, L_GI]
            # ciclo del check per una riga di tutti i duoi doppioni nella colonna
            # 'deve andare fino a L_GI-1 : deve controllare la colonna fino in fondo, ma senza modificare gli elementi prima della colonna j
            # 'ciclo di sola sostituzione: non mettere else

                

                if col_scan.iloc[k, i] == Bersaglio and avvenuta_sost.iloc[k, i] == 0:
                            
                    col_scan.iloc[k, i] = Sostituto                             
                    avvenuta_sost.iloc[k, i] = 1


    # ####################

    displaying_terminology.objects.all().delete()
    print("Eliminati tutti i dati dentro displaying_terminology!")


