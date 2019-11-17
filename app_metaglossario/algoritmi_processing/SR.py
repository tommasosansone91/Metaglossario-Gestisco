def algoritmo_SR():

    # algoritmo per standardizzare i dati prima di incatenarli nella struttura relazionale

    import numpy as np
    import pandas as pd
    from app_metaglossario.models import prepared_terminology
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
    nomi_campi_prepared_terminology = [field.name for field in prepared_terminology._meta.get_fields()]

    # elimino la colonna dell'id stabilito da python
    nomi_campi_prepared_terminology = nomi_campi_prepared_terminology[1:]

    L_GI = len(prepared_entries)
    nC = len(nomi_campi_prepared_terminology)

    print("L_GI: %s" % L_GI)
    print("nC: %s" % nC)    

    # print(nomi_campi_prepared_terminology)
    

    # creo il dataframe
    GI = pd.DataFrame(columns=nomi_campi_prepared_terminology)

    # print(GI)


    for element in prepared_entries:

        # "Lemma", "Acronimo", "Definizione", "Ambito_riferimento", "Autore_definizione", "Posizione_definizione", "Url_definizione", "Titolo_documento_fonte", "Autore_documento_fonte", "Host_documento_fonte", "Url_documento_fonte", "Commento_entry", "Data_inserimento_entry", "Id_statico_entry", "Admin_approval_switch"
        new_entry = {"Lemma":element.Lemma, "Acronimo":element.Acronimo, "Definizione":element.Definizione, "Ambito_riferimento":element.Ambito_riferimento, "Autore_definizione":element.Autore_definizione, "Posizione_definizione":element.Posizione_definizione, "Url_definizione":element.Url_definizione, "Titolo_documento_fonte":element.Titolo_documento_fonte, "Autore_documento_fonte":element.Autore_documento_fonte, "Host_documento_fonte":element.Host_documento_fonte, "Url_documento_fonte":element.Url_documento_fonte, "Commento_entry":element.Commento_entry, "Data_inserimento_entry":element.Data_inserimento_entry, "Id_statico_entry":element.Id_statico_entry, "Admin_approval_switch":element.Admin_approval_switch}
        
        GI = GI.append(new_entry, ignore_index=True)

    print("Viene generato e ordinato il dataframe che contiene la copia dei dati nel modello prepared_terminology:")

    GI = GI.sort_values(['Lemma', 'Id_statico_entry'])
    GI = GI.reset_index(drop=True)

    print(GI)



    # preparo il tabellone fatto con le tabelle di ID e campi corrispondenti adiacenti    
   

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

    print("Viene preparata la tabella di ID e terminologia Elab1")

    print("Gli ID di Elab 1 vengono assegnati in ordine numerico ascendente con l'ordine alfabetico (A->Z) di ogni colonna")

    

    Elab1 = Elab1.sort_values(['Lemma', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Lemma = IDs_prestampa.ID_db_Lemma   

    Elab1 = Elab1.sort_values(['Acronimo', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Acronimo = IDs_prestampa.ID_db_Acronimo    

    Elab1 = Elab1.sort_values(['Definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Definizione = IDs_prestampa.ID_db_Definizione

    Elab1 = Elab1.sort_values(['Ambito_riferimento', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Ambito_riferimento = IDs_prestampa.ID_db_Ambito_riferimento

    Elab1 = Elab1.sort_values(['Autore_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Autore_definizione = IDs_prestampa.ID_db_Autore_definizione

    Elab1 = Elab1.sort_values(['Posizione_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Posizione_definizione = IDs_prestampa.ID_db_Posizione_definizione

    Elab1 = Elab1.sort_values(['Url_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Url_definizione = IDs_prestampa.ID_db_Url_definizione

    Elab1 = Elab1.sort_values(['Titolo_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Titolo_documento_fonte = IDs_prestampa.ID_db_Titolo_documento_fonte

    Elab1 = Elab1.sort_values(['Autore_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Autore_documento_fonte = IDs_prestampa.ID_db_Autore_documento_fonte

    Elab1 = Elab1.sort_values(['Host_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Host_documento_fonte = IDs_prestampa.ID_db_Host_documento_fonte

    Elab1 = Elab1.sort_values(['Url_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Url_documento_fonte = IDs_prestampa.ID_db_Url_documento_fonte

    Elab1 = Elab1.sort_values(['Commento_entry', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Commento_entry = IDs_prestampa.ID_db_Commento_entry

    Elab1 = Elab1.sort_values(['Data_inserimento_entry', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Data_inserimento_entry = IDs_prestampa.ID_db_Data_inserimento_entry

    Elab1 = Elab1.sort_values(['Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Id_statico_entry = IDs_prestampa.ID_db_Id_statico_entry

    Elab1 = Elab1.sort_values(['Admin_approval_switch', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)
    Elab1.ID_db_Admin_approval_switch = IDs_prestampa.ID_db_Admin_approval_switch


    Elab1 = Elab1.sort_values(['Lemma', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    
    print(Elab1)

    # tengo traccia delle ripetizioni presenti in ogni colonna del dataframe
    label_ripetizioni = []

    for i in range(nC):
        label_ripetizioni.append("Ripetizioni_di_" + nomi_campi_prepared_terminology[i])

    ripetizioni_content = []

    for i in range(L_GI):
        ripetizioni_content.append([ 0 for j in range(nC) ])

    ripetizioni = pd.DataFrame(ripetizioni_content, columns=label_ripetizioni)
    

    # inizia la riscrittura degli id per mettere uguali queli che corrispondono ad oggetti uguali

    #ordino il glossario alfabeticamente per X

    # pone uguali id di elementi guuali

    #  If ActiveCell.Offset(j, nC).Value = ActiveCell.Offset(j - 1, nC).Value Then
                    
    #                 ActiveCell.Offset(j, 0).Value = ActiveCell.Offset(j - 1, 0)
                    
    #                 Ripetizioni(i) = Ripetizioni(i) + 1
                    
    #                 Else
                    
    #                 ActiveCell.Offset(j, 0).Value = ActiveCell.Offset(j - 1, 0) + 1
                    
    #                 End If

    # salto il fatto che id statico non ha ripetizioni perchè c'è l'interruttore di show/hide

    label_Elab1 = nomi_campi_prepared_terminology + label_IDs_prestampa

    print("Inizia lo scansionamento della terminologia e dei metadati per individuare elementi uguali...")
    
    # non posso fare il megaciclo      

    # nuovo campo da processare

    print("Ricerca dei lemmi uguali...")

    Elab1 = Elab1.sort_values(['Lemma', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Lemma"] == Elab1.at[i, "Lemma"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Lemma"] = Elab1.at[i, "ID_db_Lemma"]

    
    

    #nuovo campo da processare

    print("Ricerca degli acronimi uguali...")
    
    Elab1 = Elab1.sort_values(['Acronimo', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Acronimo"] == Elab1.at[i, "Acronimo"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Acronimo"] = Elab1.at[i, "ID_db_Acronimo"]

    #nuovo campo da processare
    
    print("Ricerca delle definizioni uguali...")

    Elab1 = Elab1.sort_values(['Definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Definizione"] == Elab1.at[i, "Definizione"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Definizione"] = Elab1.at[i, "ID_db_Definizione"]


    #nuovo campo da processare

    print("Ricerca degli ambiti di riferimento uguali...")
    
    Elab1 = Elab1.sort_values(['Ambito_riferimento', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Ambito_riferimento"] == Elab1.at[i, "Ambito_riferimento"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Ambito_riferimento"] = Elab1.at[i, "ID_db_Ambito_riferimento"]


    #nuovo campo da processare

    print("Ricerca degli ambiti di Autore_definizione uguali...")
        
    Elab1 = Elab1.sort_values(['Autore_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Autore_definizione"] == Elab1.at[i, "Autore_definizione"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Autore_definizione"] = Elab1.at[i, "ID_db_Autore_definizione"]


    #nuovo campo da processare

    print("Ricerca delle posizioni delle definizioni uguali...")
        
    Elab1 = Elab1.sort_values(['Posizione_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Posizione_definizione"] == Elab1.at[i, "Posizione_definizione"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Posizione_definizione"] = Elab1.at[i, "ID_db_Posizione_definizione"]


    #nuovo campo da processare

    print("Ricerca delgli url delle definizioni uguali...")
        
    Elab1 = Elab1.sort_values(['Url_definizione', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Url_definizione"] == Elab1.at[i, "Url_definizione"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Url_definizione"] = Elab1.at[i, "ID_db_Url_definizione"]


    #nuovo campo da processare

    print("Ricerca dei Titolo_documento_fonte uguali...")
        
    Elab1 = Elab1.sort_values(['Titolo_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Titolo_documento_fonte"] == Elab1.at[i, "Titolo_documento_fonte"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Titolo_documento_fonte"] = Elab1.at[i, "ID_db_Titolo_documento_fonte"]


#nuovo campo da processare

    print("Ricerca dei Autore_documento_fonte uguali...")
    
    Elab1 = Elab1.sort_values(['Autore_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Autore_documento_fonte"] == Elab1.at[i, "Autore_documento_fonte"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Autore_documento_fonte"] = Elab1.at[i, "ID_db_Autore_documento_fonte"]


#nuovo campo da processare

    print("Ricerca dei Host_documento_fonte uguali...")
    
    Elab1 = Elab1.sort_values(['Host_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Host_documento_fonte"] == Elab1.at[i, "Host_documento_fonte"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Host_documento_fonte"] = Elab1.at[i, "ID_db_Host_documento_fonte"]


#nuovo campo da processare

    print("Ricerca dei Url_documento_fonte uguali...")
    
    Elab1 = Elab1.sort_values(['Url_documento_fonte', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Url_documento_fonte"] == Elab1.at[i, "Url_documento_fonte"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Url_documento_fonte"] = Elab1.at[i, "ID_db_Url_documento_fonte"]


#nuovo campo da processare

    print("Ricerca dei Commento_entry uguali...")
    
    Elab1 = Elab1.sort_values(['Commento_entry', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Commento_entry"] == Elab1.at[i, "Commento_entry"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Commento_entry"] = Elab1.at[i, "ID_db_Commento_entry"]


#nuovo campo da processare

    print("Ricerca delle date_entry uguali...")
    
    Elab1 = Elab1.sort_values(['Data_inserimento_entry', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Data_inserimento_entry"] == Elab1.at[i, "Data_inserimento_entry"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Data_inserimento_entry"] = Elab1.at[i, "ID_db_Data_inserimento_entry"]


#nuovo campo da processare
    
    # Id_statico_entry slta perchè sicuramente è univoco

    # nel foglio excel di ingresso devo fare un meccanismo per assegnare gli id ma li fa l'utore


#nuovo campo da processare

    print("Ricerca degli Admin_approval_switch uguali...")
    
    Elab1 = Elab1.sort_values(['Admin_approval_switch', 'Id_statico_entry'])
    Elab1 = Elab1.reset_index(drop=True)

    # uno in meno perchè devo fare confronto tra i e i+1
    for i in range(L_GI-1):

        # se gli oggetti consecutivi sono uguali
        if Elab1.at[i+1, "Admin_approval_switch"] == Elab1.at[i, "Admin_approval_switch"] :

            # poni l'id successivo uguale a quello attuale
            Elab1.at[i+1, "ID_db_Admin_approval_switch"] = Elab1.at[i, "ID_db_Admin_approval_switch"]





    print(Elab1)

    print("Elab1 è interessato dalle seguenti ripetizioni:")

    print(ripetizioni)