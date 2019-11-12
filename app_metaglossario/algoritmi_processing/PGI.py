def algoritmo_PGI():

    import pandas as pd
    from app_metaglossario.models import acquired_terminology, prepared_terminology

    
    # database di prima elaborazione
        # oppure uso degli spazi virtuali, ossia le variabili, per ogni scrittura

    #  svuoto il database destinazione 

    prepared_terminology.objects.all().delete()

    # lista del vecchio modello
    acquired_rows = acquired_terminology.objects.all()

    print("Il modello prepared_terminology è stato svuotato")

    print("Inizia lo riempimento del modello prepared_terminology...")

    # compilo il nuovo modello coi dati 

    for element in acquired_rows:

        prepared_entry = prepared_terminology.objects.create()
        
        if not pd.isnull(element.Lemma):
            prepared_entry.Lemma = element.Lemma

        if not pd.isnull(element.Acronimo):
            prepared_entry.Acronimo = element.Acronimo

        if not pd.isnull(element.Definizione):    
            prepared_entry.Definizione = element.Definizione

        if not pd.isnull(element.Ambito_riferimento):    
            prepared_entry.Ambito_riferimento = element.Ambito_riferimento

        if not pd.isnull(element.Autore_definizione):    
            prepared_entry.Autore_definizione = element.Autore_definizione

        if not pd.isnull(element.Posizione_definizione):    
            prepared_entry.Posizione_definizione = element.Posizione_definizione

        if not pd.isnull(element.Url_definizione):    
            prepared_entry.Url_definizione = element.Url_definizione

        if not pd.isnull(element.Titolo_documento_fonte):    
            prepared_entry.Titolo_documento_fonte = element.Titolo_documento_fonte

        if not pd.isnull(element.Autore_documento_fonte):    
            prepared_entry.Autore_documento_fonte = element.Autore_documento_fonte

        if not pd.isnull(element.Host_documento_fonte):    
            prepared_entry.Host_documento_fonte = element.Host_documento_fonte

        if not pd.isnull(element.Url_documento_fonte):    
            prepared_entry.Url_documento_fonte = element.Url_documento_fonte

        if not pd.isnull(element.Commento_entry):    
            prepared_entry.Commento_entry = element.Commento_entry

            
        prepared_entry.Data_inserimento_entry = element.Data_inserimento_entry
        prepared_entry.Id_statico_entry = element.Id_statico_entry               
        prepared_entry.Admin_approval_switch = element.Admin_approval_switch

        prepared_entry.save()


    print("Riempimento del modello prepared_terminology terminato con successo!")

    print("Inizia l'elaborazione della terminologia contenuta nel modello prepared_terminology...")


    # upper, lower, title
    print("Inizia la modifica del formato del testo (uppercase/title)...")

    prepared_rows = prepared_terminology.objects.all()

    for prepared_entry in prepared_rows:

        if not pd.isnull(prepared_entry.Lemma):
            prepared_entry.Lemma.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Acronimo):
            prepared_entry.Acronimo.upper()
            
        if not pd.isnull(prepared_entry.Ambito_riferimento):    
            prepared_entry.Ambito_riferimento.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_definizione):    
            prepared_entry.Autore_definizione.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Posizione_definizione):    
            prepared_entry.Posizione_definizione.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Titolo_documento_fonte):    
            prepared_entry.Titolo_documento_fonte.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Autore_documento_fonte):    
            prepared_entry.Autore_documento_fonte.title() # non è veramente necessario

        if not pd.isnull(prepared_entry.Host_documento_fonte):    
            prepared_entry.Host_documento_fonte.title() # non è veramente necessario

        prepared_entry.Id_statico_entry.upper() 

        prepared_entry.save()
        

    print(prepared_rows)

    print("Modifica del formato del testo (uppercase/title) del modello prepared_terminology terminato con successo!")

    # cambio di maiuscole e minuscole

    # elimina spazi da davanti e dietro

    # sostituzione di doppi spazi e  acapo con degli spazi


