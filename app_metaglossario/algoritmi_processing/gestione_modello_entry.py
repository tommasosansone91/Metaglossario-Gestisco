# contiene 2 algoritmi per la gestione del modello delle singole entrate

from app_metaglossario.models import *
import pandas as pd


def pour_entire_entry_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_entire_entry_model!")

    print("Inizia il riversamento di tutti i dati dal modello glossary_entry al modello acquired_terminology!")

    elements = glossary_entry.objects.all() 
    # elementi del modello

    for element in elements:

        # copia la entry solo se l'amministrazione ha impostato che la si può mostrare
        if element.Admin_approval_switch == "show":

            # crea la entry vuota
            entry = acquired_terminology.objects.create()

            # se un element è riconosciuto come vuoto, 
            # assegna al suo corrispondente nel nuovo modello none
            # altrimenti
            # copialo normalemnte

            if not element.Lemma_it:    
                entry.Lemma_it = None
            else:   
                entry.Lemma_it = element.Lemma_it


            if not element.Acronimo_it:    
                entry.Acronimo_it = None
            else:   
                entry.Acronimo_it = element.Acronimo_it


            if not element.Definizione_it:    
                entry.Definizione_it = None
            else:
                # if not pd.isnull(element.Definizione_it):    
                entry.Definizione_it = element.Definizione_it


            if not element.Ambito_riferimento_it:    
                entry.Ambito_riferimento_it = None
            else:    
                entry.Ambito_riferimento_it = element.Ambito_riferimento_it


            if not element.Autore_definizione_it:    
                entry.Autore_definizione_it = None
            else:  
                entry.Autore_definizione_it = element.Autore_definizione_it


            if not element.Posizione_definizione_it:    
                entry.Posizione_definizione_it = None
            else:  
                entry.Posizione_definizione_it = element.Posizione_definizione_it


            if not element.Url_definizione_it:    
                entry.Url_definizione_it = None
            else:  
                entry.Url_definizione_it = element.Url_definizione_it


            if not element.Titolo_documento_fonte_it:    
                entry.Titolo_documento_fonte_it = None
            else:  
                entry.Titolo_documento_fonte_it = element.Titolo_documento_fonte_it


            if not element.Autore_documento_fonte_it:    
                entry.Autore_documento_fonte_it = None
            else:  
                entry.Autore_documento_fonte_it = element.Autore_documento_fonte_it


            if not element.Host_documento_fonte_it:    
                entry.Host_documento_fonte_it = None
            else:  
                entry.Host_documento_fonte_it = element.Host_documento_fonte_it


            if not element.Url_documento_fonte_it:    
                entry.Url_documento_fonte_it = None
            else:  
                entry.Url_documento_fonte_it = element.Url_documento_fonte_it





            if not element.Lemma_ch:    
                entry.Lemma_ch = None
            else:   
                entry.Lemma_ch = element.Lemma_ch


            if not element.Acronimo_ch:    
                entry.Acronimo_ch = None
            else:   
                entry.Acronimo_ch = element.Acronimo_ch


            if not element.Definizione_ch:    
                entry.Definizione_ch = None
            else:
                # if not pd.isnull(element.Definizione_ch):    
                entry.Definizione_ch = element.Definizione_ch


            if not element.Ambito_riferimento_ch:    
                entry.Ambito_riferimento_ch = None
            else:    
                entry.Ambito_riferimento_ch = element.Ambito_riferimento_ch


            if not element.Autore_definizione_ch:    
                entry.Autore_definizione_ch = None
            else:  
                entry.Autore_definizione_ch = element.Autore_definizione_ch


            if not element.Posizione_definizione_ch:    
                entry.Posizione_definizione_ch = None
            else:  
                entry.Posizione_definizione_ch = element.Posizione_definizione_ch


            if not element.Url_definizione_ch:    
                entry.Url_definizione_ch = None
            else:  
                entry.Url_definizione_ch = element.Url_definizione_ch


            if not element.Titolo_documento_fonte_ch:    
                entry.Titolo_documento_fonte_ch = None
            else:  
                entry.Titolo_documento_fonte_ch = element.Titolo_documento_fonte_ch


            if not element.Autore_documento_fonte_ch:    
                entry.Autore_documento_fonte_ch = None
            else:  
                entry.Autore_documento_fonte_ch = element.Autore_documento_fonte_ch


            if not element.Host_documento_fonte_ch:    
                entry.Host_documento_fonte_ch = None
            else:  
                entry.Host_documento_fonte_ch = element.Host_documento_fonte_ch


            if not element.Url_documento_fonte_ch:    
                entry.Url_documento_fonte_ch = None
            else:  
                entry.Url_documento_fonte_ch = element.Url_documento_fonte_ch




            if not element.Commento_entry:    
                entry.Commento_entry = None
            else:  
                entry.Commento_entry = element.Commento_entry

                
            entry.Data_inserimento_entry=element.Data_inserimento_entry
            entry.Id_statico_entry=element.Id_statico_entry               
            entry.Admin_approval_switch=element.Admin_approval_switch

            entry.save()



    print("Tutti i record di terminologia salvati nel modello glossary_entry sono stati riversati nel modello acquired_terminology!")






def pour_latest_entry():

    print("Viene richiamato l'algoritmo pour_latest_entry!")

    element = glossary_file.objects.latest('Data_inserimento_entry')
    
    print("Il record inserito viene riversato nel modello acquired_terminology!")    


    # copia la entry solo se l'amministrazione ha impostato che la si può mostrare
    if element.Admin_approval_switch == "show":

        # crea la entry vuota
        entry = acquired_terminology.objects.create()

        # se un element è riconosciuto come vuoto, 
        # assegna al suo corrispondente nel nuovo modello none
        # altrimenti
        # copialo normalemnte

        if not element.Lemma_it:    
            entry.Lemma_it = None
        else:   
            entry.Lemma_it = element.Lemma_it


        if not element.Acronimo_it:    
            entry.Acronimo_it = None
        else:   
            entry.Acronimo_it = element.Acronimo_it


        if not element.Definizione_it:    
            entry.Definizione_it = None
        else:
            # if not pd.isnull(element.Definizione_it):    
            entry.Definizione_it = element.Definizione_it


        if not element.Ambito_riferimento_it:    
            entry.Ambito_riferimento_it = None
        else:    
            entry.Ambito_riferimento_it = element.Ambito_riferimento_it


        if not element.Autore_definizione_it:    
            entry.Autore_definizione_it = None
        else:  
            entry.Autore_definizione_it = element.Autore_definizione_it


        if not element.Posizione_definizione_it:    
            entry.Posizione_definizione_it = None
        else:  
            entry.Posizione_definizione_it = element.Posizione_definizione_it


        if not element.Url_definizione_it:    
            entry.Url_definizione_it = None
        else:  
            entry.Url_definizione_it = element.Url_definizione_it


        if not element.Titolo_documento_fonte_it:    
            entry.Titolo_documento_fonte_it = None
        else:  
            entry.Titolo_documento_fonte_it = element.Titolo_documento_fonte_it


        if not element.Autore_documento_fonte_it:    
            entry.Autore_documento_fonte_it = None
        else:  
            entry.Autore_documento_fonte_it = element.Autore_documento_fonte_it


        if not element.Host_documento_fonte_it:    
            entry.Host_documento_fonte_it = None
        else:  
            entry.Host_documento_fonte_it = element.Host_documento_fonte_it


        if not element.Url_documento_fonte_it:    
            entry.Url_documento_fonte_it = None
        else:  
            entry.Url_documento_fonte_it = element.Url_documento_fonte_it





        if not element.Lemma_ch:    
            entry.Lemma_ch = None
        else:   
            entry.Lemma_ch = element.Lemma_ch


        if not element.Acronimo_ch:    
            entry.Acronimo_ch = None
        else:   
            entry.Acronimo_ch = element.Acronimo_ch


        if not element.Definizione_ch:    
            entry.Definizione_ch = None
        else:
            # if not pd.isnull(element.Definizione_ch):    
            entry.Definizione_ch = element.Definizione_ch


        if not element.Ambito_riferimento_ch:    
            entry.Ambito_riferimento_ch = None
        else:    
            entry.Ambito_riferimento_ch = element.Ambito_riferimento_ch


        if not element.Autore_definizione_ch:    
            entry.Autore_definizione_ch = None
        else:  
            entry.Autore_definizione_ch = element.Autore_definizione_ch


        if not element.Posizione_definizione_ch:    
            entry.Posizione_definizione_ch = None
        else:  
            entry.Posizione_definizione_ch = element.Posizione_definizione_ch


        if not element.Url_definizione_ch:    
            entry.Url_definizione_ch = None
        else:  
            entry.Url_definizione_ch = element.Url_definizione_ch


        if not element.Titolo_documento_fonte_ch:    
            entry.Titolo_documento_fonte_ch = None
        else:  
            entry.Titolo_documento_fonte_ch = element.Titolo_documento_fonte_ch


        if not element.Autore_documento_fonte_ch:    
            entry.Autore_documento_fonte_ch = None
        else:  
            entry.Autore_documento_fonte_ch = element.Autore_documento_fonte_ch


        if not element.Host_documento_fonte_ch:    
            entry.Host_documento_fonte_ch = None
        else:  
            entry.Host_documento_fonte_ch = element.Host_documento_fonte_ch


        if not element.Url_documento_fonte_ch:    
            entry.Url_documento_fonte_ch = None
        else:  
            entry.Url_documento_fonte_ch = element.Url_documento_fonte_ch




        if not element.Commento_entry:    
            entry.Commento_entry = None
        else:  
            entry.Commento_entry = element.Commento_entry

            
        entry.Data_inserimento_entry=element.Data_inserimento_entry
        entry.Id_statico_entry=element.Id_statico_entry               
        entry.Admin_approval_switch=element.Admin_approval_switch

        entry.save()

    print("Riversamento terminato con successo!")
