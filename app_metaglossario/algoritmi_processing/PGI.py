def algoritmo_PGI():

    print("Viene richiamato l'algoritmo PGI!")

    # algoritmo per standardizzare i dati prima di incatenarli nella struttura relazionale

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    import pandas as pd
    from app_metaglossario.models import acquired_terminology, prepared_terminology

    print("Inizia la standardizzazione del formato dei dati per prepararli all'inserimento nel database...")
    
    # samtlisci il algoritmo perchè vanno bene i Nan

    # database di prima elaborazione
    # ppure uso degli spazi virtuali, ossia le variabili, per ogni scrittura

    #  il database destinazione è già stato svuotato

    # lista del vecchio modello
    acquired_rows = acquired_terminology.objects.all()

    print("Il modello prepared_terminology è stato svuotato!")

    print("Inizia lo riempimento del modello prepared_terminology...")

    # compilo il nuovo modello coi dati 

    for element in acquired_rows:

        prepared_entry = prepared_terminology.objects.create()
        
        if not pd.isnull(element.Lemma_it):
            prepared_entry.Lemma_it = element.Lemma_it

        if not pd.isnull(element.Acronimo_it):
            prepared_entry.Acronimo_it = element.Acronimo_it

        if not pd.isnull(element.Definizione_it):    
            prepared_entry.Definizione_it = element.Definizione_it


        if not pd.isnull(element.Ambito_riferimento_it):    
            prepared_entry.Ambito_riferimento_it = element.Ambito_riferimento_it

        if not pd.isnull(element.Autore_definizione_it):    
            prepared_entry.Autore_definizione_it = element.Autore_definizione_it

        if not pd.isnull(element.Posizione_definizione_it):    
            prepared_entry.Posizione_definizione_it = element.Posizione_definizione_it

        if not pd.isnull(element.Url_definizione_it):    
            prepared_entry.Url_definizione_it = element.Url_definizione_it

        if not pd.isnull(element.Titolo_documento_fonte_it):    
            prepared_entry.Titolo_documento_fonte_it = element.Titolo_documento_fonte_it

        if not pd.isnull(element.Autore_documento_fonte_it):    
            prepared_entry.Autore_documento_fonte_it = element.Autore_documento_fonte_it

        if not pd.isnull(element.Host_documento_fonte_it):    
            prepared_entry.Host_documento_fonte_it = element.Host_documento_fonte_it

        if not pd.isnull(element.Url_documento_fonte_it):    
            prepared_entry.Url_documento_fonte_it = element.Url_documento_fonte_it


        if not pd.isnull(element.Lemma_ch):
            prepared_entry.Lemma_ch = element.Lemma_ch

        if not pd.isnull(element.Acronimo_ch):
            prepared_entry.Acronimo_ch = element.Acronimo_ch

        if not pd.isnull(element.Definizione_ch):    
            prepared_entry.Definizione_ch = element.Definizione_ch

        if not pd.isnull(element.Ambito_riferimento_ch):    
            prepared_entry.Ambito_riferimento_ch = element.Ambito_riferimento_ch

        if not pd.isnull(element.Autore_definizione_ch):    
            prepared_entry.Autore_definizione_ch = element.Autore_definizione_ch

        if not pd.isnull(element.Posizione_definizione_ch):    
            prepared_entry.Posizione_definizione_ch = element.Posizione_definizione_ch

        if not pd.isnull(element.Url_definizione_ch):    
            prepared_entry.Url_definizione_ch = element.Url_definizione_ch

        if not pd.isnull(element.Titolo_documento_fonte_ch):    
            prepared_entry.Titolo_documento_fonte_ch = element.Titolo_documento_fonte_ch

        if not pd.isnull(element.Autore_documento_fonte_ch):    
            prepared_entry.Autore_documento_fonte_ch = element.Autore_documento_fonte_ch

        if not pd.isnull(element.Host_documento_fonte_ch):    
            prepared_entry.Host_documento_fonte_ch = element.Host_documento_fonte_ch

        if not pd.isnull(element.Url_documento_fonte_ch):    
            prepared_entry.Url_documento_fonte_ch = element.Url_documento_fonte_ch



        if not pd.isnull(element.Commento_entry):    
            prepared_entry.Commento_entry = element.Commento_entry


            
        prepared_entry.Data_inserimento_entry = element.Data_inserimento_entry
        prepared_entry.Id_statico_entry = element.Id_statico_entry               
        prepared_entry.Admin_approval_switch = element.Admin_approval_switch

        prepared_entry.save()


    print("Riempimento del modello prepared_terminology terminato con successo!")

    print("Inizia l'elaborazione della terminologia contenuta nel modello prepared_terminology...")




    # sostituzione di doppi spazi e a capo con degli spazi

    print("Inizia l'eliminazione dei doppi spazi dal testo...")
    
    rip_doppi_spazi = 3 # ripeto il ciclo 3 volte 

    prepared_rows = prepared_terminology.objects.all()

    # sostituzione di doppi spazi con degli spazi singoli
    for i in range(rip_doppi_spazi):    # ripeto il ciclo n volte 

        for prepared_entry in prepared_rows:      
            
            if not pd.isnull(prepared_entry.Lemma_it):
                prepared_entry.Lemma_it = prepared_entry.Lemma_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Acronimo_it):
                prepared_entry.Acronimo_it = prepared_entry.Acronimo_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Definizione_it):    
                prepared_entry.Definizione_it = prepared_entry.Definizione_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Ambito_riferimento_it):    
                prepared_entry.Ambito_riferimento_it = prepared_entry.Ambito_riferimento_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_definizione_it):    
                prepared_entry.Autore_definizione_it = prepared_entry.Autore_definizione_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Posizione_definizione_it):    
                prepared_entry.Posizione_definizione_it = prepared_entry.Posizione_definizione_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Titolo_documento_fonte_it):    
                prepared_entry.Titolo_documento_fonte_it = prepared_entry.Titolo_documento_fonte_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_documento_fonte_it):    
                prepared_entry.Autore_documento_fonte_it = prepared_entry.Autore_documento_fonte_it.replace("  ", " ")

            if not pd.isnull(prepared_entry.Host_documento_fonte_it):    
                prepared_entry.Host_documento_fonte_it = prepared_entry.Host_documento_fonte_it.replace("  ", " ")
            

            if not pd.isnull(prepared_entry.Lemma_ch):
                prepared_entry.Lemma_ch = prepared_entry.Lemma_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Acronimo_ch):
                prepared_entry.Acronimo_ch = prepared_entry.Acronimo_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Definizione_ch):    
                prepared_entry.Definizione_ch = prepared_entry.Definizione_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Ambito_riferimento_ch):    
                prepared_entry.Ambito_riferimento_ch = prepared_entry.Ambito_riferimento_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_definizione_ch):    
                prepared_entry.Autore_definizione_ch = prepared_entry.Autore_definizione_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Posizione_definizione_ch):    
                prepared_entry.Posizione_definizione_ch = prepared_entry.Posizione_definizione_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Titolo_documento_fonte_ch):    
                prepared_entry.Titolo_documento_fonte_ch = prepared_entry.Titolo_documento_fonte_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Autore_documento_fonte_ch):    
                prepared_entry.Autore_documento_fonte_ch = prepared_entry.Autore_documento_fonte_ch.replace("  ", " ")

            if not pd.isnull(prepared_entry.Host_documento_fonte_ch):    
                prepared_entry.Host_documento_fonte_ch = prepared_entry.Host_documento_fonte_ch.replace("  ", " ")
            


            if not pd.isnull(prepared_entry.Commento_entry):    
                prepared_entry.Commento_entry = prepared_entry.Commento_entry.replace("  ", " ")                      
        

            # non possono esserci doppi spazi in data, id e switch

            prepared_entry.save()



    # elimina spazi da davanti e dietro


    print("Eliminazione dei doppi spazi terminata con successo!")
    print("Inizia l'eliminazione degli spazi all'inizio e alla fine di ogni cella...")

    # prepared_rows = prepared_terminology.objects.all()

    for prepared_entry in prepared_rows:       
        
        if not pd.isnull(prepared_entry.Lemma_it):
            if prepared_entry.Lemma_it[0] == " ":
                prepared_entry.Lemma_it = prepared_entry.Lemma_it[1:]
            if prepared_entry.Lemma_it[-1] == " ":
                prepared_entry.Lemma_it = prepared_entry.Lemma_it[0:-1]
                
        if not pd.isnull(prepared_entry.Acronimo_it):
            if prepared_entry.Acronimo_it[0] == " ":
                prepared_entry.Acronimo_it = prepared_entry.Acronimo_it[1:]
            if prepared_entry.Acronimo_it[-1] == " ":
                prepared_entry.Acronimo_it = prepared_entry.Acronimo_it[0:-1]

        if not pd.isnull(prepared_entry.Definizione_it):   
            if prepared_entry.Definizione_it[0] == " ":
                prepared_entry.Definizione_it = prepared_entry.Definizione_it[1:]
            if prepared_entry.Definizione_it[-1] == " ":
                prepared_entry.Definizione_it = prepared_entry.Definizione_it[0:-1]

        if not pd.isnull(prepared_entry.Ambito_riferimento_it):    
            if prepared_entry.Ambito_riferimento_it[0] == " ":
                prepared_entry.Ambito_riferimento_it = prepared_entry.Ambito_riferimento_it[1:]
            if prepared_entry.Ambito_riferimento_it[-1] == " ":
                prepared_entry.Ambito_riferimento_it = prepared_entry.Ambito_riferimento_it[0:-1]

        if not pd.isnull(prepared_entry.Autore_definizione_it):    
            if prepared_entry.Autore_definizione_it[0] == " ":
                prepared_entry.Autore_definizione_it = prepared_entry.Autore_definizione_it[1:]
            if prepared_entry.Autore_definizione_it[-1] == " ":
                prepared_entry.Autore_definizione_it = prepared_entry.Autore_definizione_it[0:-1]

        if not pd.isnull(prepared_entry.Posizione_definizione_it):    
            if prepared_entry.Posizione_definizione_it[0] == " ":
                prepared_entry.Posizione_definizione_it = prepared_entry.Posizione_definizione_it[1:]
            if prepared_entry.Posizione_definizione_it[-1] == " ":
                prepared_entry.Posizione_definizione_it = prepared_entry.Posizione_definizione_it[0:-1]

        if not pd.isnull(prepared_entry.Url_definizione_it):    
            if prepared_entry.Url_definizione_it[0] == " ":
                prepared_entry.Url_definizione_it = prepared_entry.Url_definizione_it[1:]
            if prepared_entry.Url_definizione_it[-1] == " ":
                prepared_entry.Url_definizione_it = prepared_entry.Url_definizione_it[0:-1]

        if not pd.isnull(prepared_entry.Titolo_documento_fonte_it):    
            if prepared_entry.Titolo_documento_fonte_it[0] == " ":
                prepared_entry.Titolo_documento_fonte_it = prepared_entry.Titolo_documento_fonte_it[1:]
            if prepared_entry.Titolo_documento_fonte_it[-1] == " ":
                prepared_entry.Titolo_documento_fonte_it = prepared_entry.Titolo_documento_fonte_it[0:-1]

        if not pd.isnull(prepared_entry.Autore_documento_fonte_it):    
            if prepared_entry.Autore_documento_fonte_it[0] == " ":
                prepared_entry.Autore_documento_fonte_it = prepared_entry.Autore_documento_fonte_it[1:]
            if prepared_entry.Autore_documento_fonte_it[-1] == " ":
                prepared_entry.Autore_documento_fonte_it = prepared_entry.Autore_documento_fonte_it[0:-1]

        if not pd.isnull(prepared_entry.Host_documento_fonte_it):    
            if prepared_entry.Host_documento_fonte_it[0] == " ":
                prepared_entry.Host_documento_fonte_it = prepared_entry.Host_documento_fonte_it[1:]
            if prepared_entry.Host_documento_fonte_it[-1] == " ":
                prepared_entry.Host_documento_fonte_it = prepared_entry.Host_documento_fonte_it[0:-1]

        if not pd.isnull(prepared_entry.Url_documento_fonte_it):    
            if prepared_entry.Url_documento_fonte_it[0] == " ":
                prepared_entry.Url_documento_fonte_it = prepared_entry.Url_documento_fonte_it[1:]
            if prepared_entry.Url_documento_fonte_it[-1] == " ":
                prepared_entry.Url_documento_fonte_it = prepared_entry.Url_documento_fonte_it[0:-1]



        if not pd.isnull(prepared_entry.Lemma_ch):
            if prepared_entry.Lemma_ch[0] == " ":
                prepared_entry.Lemma_ch = prepared_entry.Lemma_ch[1:]
            if prepared_entry.Lemma_ch[-1] == " ":
                prepared_entry.Lemma_ch = prepared_entry.Lemma_ch[0:-1]

        if not pd.isnull(prepared_entry.Acronimo_ch):
            if prepared_entry.Acronimo_ch[0] == " ":
                prepared_entry.Acronimo_ch = prepared_entry.Acronimo_ch[1:]
            if prepared_entry.Acronimo_ch[-1] == " ":
                prepared_entry.Acronimo_ch = prepared_entry.Acronimo_ch[0:-1]

        if not pd.isnull(prepared_entry.Definizione_ch):    
            if prepared_entry.Definizione_ch[0] == " ":
                prepared_entry.Definizione_ch = prepared_entry.Definizione_ch[1:]
            if prepared_entry.Definizione_ch[-1] == " ":
                prepared_entry.Definizione_ch = prepared_entry.Definizione_ch[0:-1]

        if not pd.isnull(prepared_entry.Ambito_riferimento_ch):    
            if prepared_entry.Ambito_riferimento_ch[0] == " ":
                prepared_entry.Ambito_riferimento_ch = prepared_entry.Ambito_riferimento_ch[1:]
            if prepared_entry.Ambito_riferimento_ch[-1] == " ":
                prepared_entry.Ambito_riferimento_ch = prepared_entry.Ambito_riferimento_ch[0:-1]

        if not pd.isnull(prepared_entry.Autore_definizione_ch):    
            if prepared_entry.Autore_definizione_ch[0] == " ":
                prepared_entry.Autore_definizione_ch = prepared_entry.Autore_definizione_ch[1:]
            if prepared_entry.Autore_definizione_ch[-1] == " ":
                prepared_entry.Autore_definizione_ch = prepared_entry.Autore_definizione_ch[0:-1]

        if not pd.isnull(prepared_entry.Posizione_definizione_ch):    
            if prepared_entry.Posizione_definizione_ch[0] == " ":
                prepared_entry.Posizione_definizione_ch = prepared_entry.Posizione_definizione_ch[1:]
            if prepared_entry.Posizione_definizione_ch[-1] == " ":
                prepared_entry.Posizione_definizione_ch = prepared_entry.Posizione_definizione_ch[0:-1]

        if not pd.isnull(prepared_entry.Url_definizione_ch):    
            if prepared_entry.Url_definizione_ch[0] == " ":
                prepared_entry.Url_definizione_ch = prepared_entry.Url_definizione_ch[1:]
            if prepared_entry.Url_definizione_ch[-1] == " ":
                prepared_entry.Url_definizione_ch = prepared_entry.Url_definizione_ch[0:-1]

        if not pd.isnull(prepared_entry.Titolo_documento_fonte_ch):    
            if prepared_entry.Titolo_documento_fonte_ch[0] == " ":
                prepared_entry.Titolo_documento_fonte_ch = prepared_entry.Titolo_documento_fonte_ch[1:]
            if prepared_entry.Titolo_documento_fonte_ch[-1] == " ":
                prepared_entry.Titolo_documento_fonte_ch = prepared_entry.Titolo_documento_fonte_ch[0:-1]

        if not pd.isnull(prepared_entry.Autore_documento_fonte_ch):    
            if prepared_entry.Autore_documento_fonte_ch[0] == " ":
                prepared_entry.Autore_documento_fonte_ch = prepared_entry.Autore_documento_fonte_ch[1:]
            if prepared_entry.Autore_documento_fonte_ch[-1] == " ":
                prepared_entry.Autore_documento_fonte_ch = prepared_entry.Autore_documento_fonte_ch[0:-1]

        if not pd.isnull(prepared_entry.Host_documento_fonte_ch):    
            if prepared_entry.Host_documento_fonte_ch[0] == " ":
                prepared_entry.Host_documento_fonte_ch = prepared_entry.Host_documento_fonte_ch[1:]
            if prepared_entry.Host_documento_fonte_ch[-1] == " ":
                prepared_entry.Host_documento_fonte_ch = prepared_entry.Host_documento_fonte_ch[0:-1]

        if not pd.isnull(prepared_entry.Url_documento_fonte_ch):    
            if prepared_entry.Url_documento_fonte_ch[0] == " ":
                prepared_entry.Url_documento_fonte_ch = prepared_entry.Url_documento_fonte_ch[1:]
            if prepared_entry.Url_documento_fonte_ch[-1] == " ":
                prepared_entry.Url_documento_fonte_ch = prepared_entry.Url_documento_fonte_ch[0:-1]




        if not pd.isnull(prepared_entry.Commento_entry):    
            if prepared_entry.Commento_entry[0] == " ":
                prepared_entry.Commento_entry = prepared_entry.Commento_entry[1:]
            if prepared_entry.Commento_entry[-1] == " ":
                prepared_entry.Commento_entry = prepared_entry.Commento_entry[0:-1]
        
        if not pd.isnull(prepared_entry.Id_statico_entry):
            if prepared_entry.Id_statico_entry[0] == " ":
                prepared_entry.Id_statico_entry = prepared_entry.Id_statico_entry[1:]
            if prepared_entry.Id_statico_entry[-1] == " ":
                prepared_entry.Id_statico_entry = prepared_entry.Id_statico_entry[0:-1]       


        prepared_entry.save()

    print("Eliminazione degli spazi all'inizio e alla fine di ogni cella terminata con successo!")


        # upper, lower, title
    print("Inizia la modifica del formato del testo (uppercase/title)...")

    prepared_rows = prepared_terminology.objects.all()

    for prepared_entry in prepared_rows:

        if not pd.isnull(prepared_entry.Lemma_it):
            prepared_entry.Lemma_it = prepared_entry.Lemma_it[:1].upper() + prepared_entry.Lemma_it[1:]

        if not pd.isnull(prepared_entry.Acronimo_it):
            prepared_entry.Acronimo_it.upper()
            
        if not pd.isnull(prepared_entry.Ambito_riferimento_it):    
            prepared_entry.Ambito_riferimento_it = prepared_entry.Ambito_riferimento_it[:1].upper() + prepared_entry.Ambito_riferimento_it[1:]

        if not pd.isnull(prepared_entry.Autore_definizione_it):    
            prepared_entry.Autore_definizione_it.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Posizione_definizione_it):    
            prepared_entry.Posizione_definizione_it = prepared_entry.Posizione_definizione_it[:1].upper() + prepared_entry.Posizione_definizione_it[1:] # non è veramente necessario

        if not pd.isnull(prepared_entry.Titolo_documento_fonte_it):    
            prepared_entry.Titolo_documento_fonte_it = prepared_entry.Titolo_documento_fonte_it[:1].upper() + prepared_entry.Titolo_documento_fonte_it[1:] # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_documento_fonte_it):    
            prepared_entry.Autore_documento_fonte_it.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Host_documento_fonte_it):    
            prepared_entry.Host_documento_fonte_it.title() # non è veramente necessario


        if not pd.isnull(prepared_entry.Lemma_ch):
            prepared_entry.Lemma_ch = prepared_entry.Lemma_ch[:1].upper() + prepared_entry.Lemma_ch[1:]

        if not pd.isnull(prepared_entry.Acronimo_ch):
            prepared_entry.Acronimo_ch.upper()
            
        if not pd.isnull(prepared_entry.Ambito_riferimento_ch):    
            prepared_entry.Ambito_riferimento_ch = prepared_entry.Ambito_riferimento_ch[:1].upper() + prepared_entry.Ambito_riferimento_ch[1:]

        if not pd.isnull(prepared_entry.Autore_definizione_ch):    
            prepared_entry.Autore_definizione_ch.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Posizione_definizione_ch):    
            prepared_entry.Posizione_definizione_ch = prepared_entry.Posizione_definizione_ch[:1].upper() + prepared_entry.Posizione_definizione_ch[1:] # non è veramente necessario

        if not pd.isnull(prepared_entry.Titolo_documento_fonte_ch):    
            prepared_entry.Titolo_documento_fonte_ch = prepared_entry.Titolo_documento_fonte_ch[:1].upper() + prepared_entry.Titolo_documento_fonte_ch[1:] # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_documento_fonte_ch):    
            prepared_entry.Autore_documento_fonte_ch.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Host_documento_fonte_ch):    
            prepared_entry.Host_documento_fonte_ch.title() # non è veramente necessario



        prepared_entry.Id_statico_entry.upper() 

        prepared_entry.save() 

       

    print("Modifica del formato del testo (uppercase/title) terminato con successo!")





    print("Standardizzazione del formato dei dati terminata con successo!")

    print("I dati sono ora in un formato standard e possono essere processati per la realizzazione della struttura relazionale!")

