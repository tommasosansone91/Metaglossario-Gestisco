from app_metaglossario.models import *

import pandas as pd



def pour_entire_entry_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_entire_entry_model!")

    print("Inizia il riversamento di tutti i dati dal modello glossary_entry al modello acquired_terminology!")

    # uso un foglio virtuale per evitare il problema dei none/vuoti
    # salvo la terminologia del modello delle singole entry in un dataframe "glossario"
    # sfrutto il codice già generato per l'algoritmo che riversa i glossari uno ad uno
    # per copiare la terminologia dal dataframe in un modello
    # in questo modo sono sicuro che la terminologia dei due modelli viene processata allo stesso modo

    print("Viene generato il foglio excel virtuale")

    all_entries = glossary_entry.objects.all() 

    # this generates an array containing the names of the model fields
    columns_names = [field.name for field in glossary_entry._meta.get_fields()]

    L_foglio_virtuale = len(all_entries)

    # generate empty dataframe, assigning name to its columns
    foglio_virtuale = pd.DataFrame(columns = columns_names)

    for element in all_entries:       
        new_entry = {"Lemma_it":element.Lemma_it, "Acronimo_it":element.Acronimo_it, "Definizione_it":element.Definizione_it, "Ambito_riferimento_it":element.Ambito_riferimento_it, "Autore_definizione_it":element.Autore_definizione_it, "Posizione_definizione_it":element.Posizione_definizione_it, "Url_definizione_it":element.Url_definizione_it, "Titolo_documento_fonte_it":element.Titolo_documento_fonte_it, "Autore_documento_fonte_it":element.Autore_documento_fonte_it, "Host_documento_fonte_it":element.Host_documento_fonte_it, "Url_documento_fonte_it":element.Url_documento_fonte_it, "Lemma_ch":element.Lemma_ch, "Acronimo_ch":element.Acronimo_ch, "Definizione_ch":element.Definizione_ch, "Ambito_riferimento_ch":element.Ambito_riferimento_ch, "Autore_definizione_ch":element.Autore_definizione_ch, "Posizione_definizione_ch":element.Posizione_definizione_ch, "Url_definizione_ch":element.Url_definizione_ch, "Titolo_documento_fonte_ch":element.Titolo_documento_fonte_ch, "Autore_documento_fonte_ch":element.Autore_documento_fonte_ch, "Host_documento_fonte_ch":element.Host_documento_fonte_ch, "Url_documento_fonte_ch":element.Url_documento_fonte_ch, "Commento_entry":element.Commento_entry, "Data_inserimento_entry":element.Data_inserimento_entry, "Id_statico_entry":element.Id_statico_entry, "Admin_approval_switch":element.Admin_approval_switch}
        foglio_virtuale = foglio_virtuale.append(new_entry, ignore_index=True)

    foglio_virtuale = foglio_virtuale.sort_values(['Lemma_it','Lemma_ch', 'Id_statico_entry'])
    foglio_virtuale = foglio_virtuale.reset_index(drop=True)

    print("*****")
    print(foglio_virtuale)
    print("*****")

        
    print("Sbobinatura del dataframe in vettori...")        
        
    col_lemma_it = foglio_virtuale.Lemma_it
    col_acronimo_it = foglio_virtuale.Acronimo_it
    col_definizione_it = foglio_virtuale.Definizione_it
    col_ambito_riferimento_it = foglio_virtuale.Ambito_riferimento_it
    col_autore_definizione_it = foglio_virtuale.Autore_definizione_it
    col_posizione_definizione_it = foglio_virtuale.Posizione_definizione_it
    col_url_definizione_it = foglio_virtuale.Url_definizione_it
    col_titolo_documento_fonte_it = foglio_virtuale.Titolo_documento_fonte_it
    col_autore_documento_fonte_it = foglio_virtuale.Autore_documento_fonte_it
    col_host_documento_fonte_it = foglio_virtuale.Host_documento_fonte_it
    col_url_documento_fonte_it = foglio_virtuale.Url_documento_fonte_it


    print(col_definizione_it)


    col_lemma_ch = foglio_virtuale.Lemma_it
    col_acronimo_ch = foglio_virtuale.Acronimo_ch
    col_definizione_ch = foglio_virtuale.Definizione_ch
    col_ambito_riferimento_ch = foglio_virtuale.Ambito_riferimento_ch
    col_autore_definizione_ch = foglio_virtuale.Autore_definizione_ch
    col_posizione_definizione_ch = foglio_virtuale.Posizione_definizione_ch
    col_url_definizione_ch = foglio_virtuale.Url_definizione_ch
    col_titolo_documento_fonte_ch = foglio_virtuale.Titolo_documento_fonte_ch
    col_autore_documento_fonte_ch = foglio_virtuale.Autore_documento_fonte_ch
    col_host_documento_fonte_ch = foglio_virtuale.Host_documento_fonte_ch
    col_url_documento_fonte_ch = foglio_virtuale.Url_documento_fonte_ch


    col_commento_entry = foglio_virtuale.Commento_entry
    col_data_inserimento_entry = foglio_virtuale.Data_inserimento_entry
    col_id_statico_entry = foglio_virtuale.Id_statico_entry
    col_admin_approval_switch = foglio_virtuale.Admin_approval_switch





    print("Inizia il riversamento di dati dal foglio virtuale al modello acquired_terminology...")

    for i in range(len(col_lemma_it)):

    # assegna i valori agli attributi uno per uno per evitare i NaN
        
        entry = acquired_terminology.objects.create()
        
        if not pd.isnull(col_lemma_it[i]):
            entry.Lemma_it = col_lemma_it[i]

        if not pd.isnull(col_acronimo_it[i]):
            entry.Acronimo_it = col_acronimo_it[i]

        if not pd.isnull(col_definizione_it[i]):  
            entry.Definizione_it = col_definizione_it[i]

        if not pd.isnull(col_ambito_riferimento_it[i]):  
            entry.Ambito_riferimento_it = col_ambito_riferimento_it[i]

        if not pd.isnull(col_autore_definizione_it[i]):  
            entry.Autore_definizione_it = col_autore_definizione_it[i]

        if not pd.isnull(col_posizione_definizione_it[i]):  
            entry.Posizione_definizione_it = col_posizione_definizione_it[i]

        if not pd.isnull(col_url_definizione_it[i]):  
            entry.Url_definizione_it = col_url_definizione_it[i]

        if not pd.isnull(col_titolo_documento_fonte_it[i]):  
            entry.Titolo_documento_fonte_it = col_titolo_documento_fonte_it[i]

        if not pd.isnull(col_autore_documento_fonte_it[i]):  
            entry.Autore_documento_fonte_it = col_autore_documento_fonte_it[i]

        if not pd.isnull(col_host_documento_fonte_it[i]):  
            entry.Host_documento_fonte_it = col_host_documento_fonte_it[i]

        if not pd.isnull(col_url_documento_fonte_it[i]):  
            entry.Url_documento_fonte_it = col_url_documento_fonte_it[i]


        if not pd.isnull(col_lemma_ch[i]):
            entry.Lemma_ch = col_lemma_ch[i]

        if not pd.isnull(col_acronimo_ch[i]):
            entry.Acronimo_ch = col_acronimo_ch[i]

        if not pd.isnull(col_definizione_ch[i]):  
            entry.Definizione_ch = col_definizione_ch[i]

        if not pd.isnull(col_ambito_riferimento_ch[i]):  
            entry.Ambito_riferimento_ch = col_ambito_riferimento_ch[i]

        if not pd.isnull(col_autore_definizione_ch[i]):  
            entry.Autore_definizione_ch = col_autore_definizione_ch[i]

        if not pd.isnull(col_posizione_definizione_ch[i]):  
            entry.Posizione_definizione_ch = col_posizione_definizione_ch[i]

        if not pd.isnull(col_url_definizione_ch[i]):  
            entry.Url_definizione_ch = col_url_definizione_ch[i]

        if not pd.isnull(col_titolo_documento_fonte_ch[i]):  
            entry.Titolo_documento_fonte_ch = col_titolo_documento_fonte_ch[i]

        if not pd.isnull(col_autore_documento_fonte_ch[i]):  
            entry.Autore_documento_fonte_ch = col_autore_documento_fonte_ch[i]

        if not pd.isnull(col_host_documento_fonte_ch[i]):  
            entry.Host_documento_fonte_ch = col_host_documento_fonte_ch[i]

        if not pd.isnull(col_url_documento_fonte_ch[i]):  
            entry.Url_documento_fonte_ch = col_url_documento_fonte_ch[i]



        if not pd.isnull(col_commento_entry[i]):    
            entry.Commento_entry = col_commento_entry[i]

            
        entry.Data_inserimento_entry = col_data_inserimento_entry[i]
        entry.Id_statico_entry = col_id_statico_entry[i]               
        entry.Admin_approval_switch = col_admin_approval_switch[i]

        entry.save()


    print("Tutti i record di terminologia salvati nel modello glossary_entry sono stati riversati nel modello acquired_terminology!")



def pour_entire_file_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_entire_file_model!")

    print("Inizia il riversamento della terminologia di tutti i file salvati nel modello glossary_file verso il modello acquired_terminology...")

    # tutti gli oggetti nel modello glossario sono salvati qui
    all_files = glossary_file.objects.all()
    
    for file_element in all_files: 
   
        # per ogni foglio nel modello
        print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % file_element.Glossary_file)
        
        # accedo all'attributo file del modello
        # salva il contenuto del file in una variabile = dataframe
        excel_sheet = pd.read_excel(file_element.Glossary_file)

        print("*****") 
        print(excel_sheet)
        print("*****")       

        print("Sbobinatura del dataframe in vettori...")        
        
        col_lemma_it = excel_sheet.Lemma_it
        col_acronimo_it = excel_sheet.Acronimo_it
        col_definizione_it = excel_sheet.Definizione_it
        col_ambito_riferimento_it = excel_sheet.Ambito_riferimento_it
        col_autore_definizione_it = excel_sheet.Autore_definizione_it
        col_posizione_definizione_it = excel_sheet.Posizione_definizione_it
        col_url_definizione_it = excel_sheet.Url_definizione_it
        col_titolo_documento_fonte_it = excel_sheet.Titolo_documento_fonte_it
        col_autore_documento_fonte_it = excel_sheet.Autore_documento_fonte_it
        col_host_documento_fonte_it = excel_sheet.Host_documento_fonte_it
        col_url_documento_fonte_it = excel_sheet.Url_documento_fonte_it

        col_lemma_ch = excel_sheet.Lemma_it
        col_acronimo_ch = excel_sheet.Acronimo_ch
        col_definizione_ch = excel_sheet.Definizione_ch
        col_ambito_riferimento_ch = excel_sheet.Ambito_riferimento_ch
        col_autore_definizione_ch = excel_sheet.Autore_definizione_ch
        col_posizione_definizione_ch = excel_sheet.Posizione_definizione_ch
        col_url_definizione_ch = excel_sheet.Url_definizione_ch
        col_titolo_documento_fonte_ch = excel_sheet.Titolo_documento_fonte_ch
        col_autore_documento_fonte_ch = excel_sheet.Autore_documento_fonte_ch
        col_host_documento_fonte_ch = excel_sheet.Host_documento_fonte_ch
        col_url_documento_fonte_ch = excel_sheet.Url_documento_fonte_ch


        col_commento_entry = excel_sheet.Commento_entry
        col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
        col_id_statico_entry = excel_sheet.Id_statico_entry
        col_admin_approval_switch = excel_sheet.Admin_approval_switch


        print("Inizia il riversamento di dati dal foglio %s al modello acquired_terminology..." % file_element.Glossary_file)

        for i in range(len(col_lemma_it)):

        # assegna i valori agli attributi uno per uno per evitare i NaN
            
            entry = acquired_terminology.objects.create()
            
            if not pd.isnull(col_lemma_it[i]):
                entry.Lemma_it = col_lemma_it[i]

            if not pd.isnull(col_acronimo_it[i]):
                entry.Acronimo_it = col_acronimo_it[i]

            if not pd.isnull(col_definizione_it[i]):  
                entry.Definizione_it = col_definizione_it[i]

            if not pd.isnull(col_ambito_riferimento_it[i]):  
                entry.Ambito_riferimento_it = col_ambito_riferimento_it[i]

            if not pd.isnull(col_autore_definizione_it[i]):  
                entry.Autore_definizione_it = col_autore_definizione_it[i]

            if not pd.isnull(col_posizione_definizione_it[i]):  
                entry.Posizione_definizione_it = col_posizione_definizione_it[i]

            if not pd.isnull(col_url_definizione_it[i]):  
                entry.Url_definizione_it = col_url_definizione_it[i]

            if not pd.isnull(col_titolo_documento_fonte_it[i]):  
                entry.Titolo_documento_fonte_it = col_titolo_documento_fonte_it[i]

            if not pd.isnull(col_autore_documento_fonte_it[i]):  
                entry.Autore_documento_fonte_it = col_autore_documento_fonte_it[i]

            if not pd.isnull(col_host_documento_fonte_it[i]):  
                entry.Host_documento_fonte_it = col_host_documento_fonte_it[i]

            if not pd.isnull(col_url_documento_fonte_it[i]):  
                entry.Url_documento_fonte_it = col_url_documento_fonte_it[i]


            if not pd.isnull(col_lemma_ch[i]):
                entry.Lemma_ch = col_lemma_ch[i]

            if not pd.isnull(col_acronimo_ch[i]):
                entry.Acronimo_ch = col_acronimo_ch[i]

            if not pd.isnull(col_definizione_ch[i]):  
                entry.Definizione_ch = col_definizione_ch[i]

            if not pd.isnull(col_ambito_riferimento_ch[i]):  
                entry.Ambito_riferimento_ch = col_ambito_riferimento_ch[i]

            if not pd.isnull(col_autore_definizione_ch[i]):  
                entry.Autore_definizione_ch = col_autore_definizione_ch[i]

            if not pd.isnull(col_posizione_definizione_ch[i]):  
                entry.Posizione_definizione_ch = col_posizione_definizione_ch[i]

            if not pd.isnull(col_url_definizione_ch[i]):  
                entry.Url_definizione_ch = col_url_definizione_ch[i]

            if not pd.isnull(col_titolo_documento_fonte_ch[i]):  
                entry.Titolo_documento_fonte_ch = col_titolo_documento_fonte_ch[i]

            if not pd.isnull(col_autore_documento_fonte_ch[i]):  
                entry.Autore_documento_fonte_ch = col_autore_documento_fonte_ch[i]

            if not pd.isnull(col_host_documento_fonte_ch[i]):  
                entry.Host_documento_fonte_ch = col_host_documento_fonte_ch[i]

            if not pd.isnull(col_url_documento_fonte_ch[i]):  
                entry.Url_documento_fonte_ch = col_url_documento_fonte_ch[i]



            if not pd.isnull(col_commento_entry[i]):    
                entry.Commento_entry = col_commento_entry[i]

                
            entry.Data_inserimento_entry = col_data_inserimento_entry[i]
            entry.Id_statico_entry = col_id_statico_entry[i]               
            entry.Admin_approval_switch = col_admin_approval_switch[i]

            entry.save()


        print("Riversamento dei dati di %s terminato con successo!" % file_element.Glossary_file)
        print("*****")
    
        
    print("La terminologia di tutti i file salvati nel modello glossary_file è stata riversata nel modello acquired_terminology!")





def pour_latest_entry():

    print("Viene richiamato l'algoritmo pour_latest_entry!")
    
    print("Il record inserito viene riversato nel modello acquired_terminology!")


    element = glossary_entry.objects.latest('Data_inserimento_entry')

    entry = acquired_terminology.objects.create()
        
    if not pd.isnull(element.Lemma_it):
        entry.Lemma_it = element.Lemma_it

    if not pd.isnull(element.Acronimo_it):
        entry.Acronimo_it = element.Acronimo_it

    if not pd.isnull(element.Definizione_it):    
        entry.Definizione_it = element.Definizione_it

    if not pd.isnull(element.Ambito_riferimento_it):    
        entry.Ambito_riferimento_it = element.Ambito_riferimento_it

    if not pd.isnull(element.Autore_definizione_it):    
        entry.Autore_definizione_it = element.Autore_definizione_it

    if not pd.isnull(element.Posizione_definizione_it):    
        entry.Posizione_definizione_it = element.Posizione_definizione_it

    if not pd.isnull(element.Url_definizione_it):    
        entry.Url_definizione_it = element.Url_definizione_it

    if not pd.isnull(element.Titolo_documento_fonte_it):    
        entry.Titolo_documento_fonte_it = element.Titolo_documento_fonte_it

    if not pd.isnull(element.Autore_documento_fonte_it):    
        entry.Autore_documento_fonte_it = element.Autore_documento_fonte_it

    if not pd.isnull(element.Host_documento_fonte_it):    
        entry.Host_documento_fonte_it = element.Host_documento_fonte_it

    if not pd.isnull(element.Url_documento_fonte):    
        entry.Url_documento_fonte_it = element.Url_documento_fonte_it

    if not pd.isnull(element.Lemma_ch):
        entry.Lemma_ch = element.Lemma_ch

    if not pd.isnull(element.Acronimo_ch):
        entry.Acronimo_ch = element.Acronimo_ch

    if not pd.isnull(element.Definizione_ch):    
        entry.Definizione_ch = element.Definizione_ch

    if not pd.isnull(element.Ambito_riferimento_ch):    
        entry.Ambito_riferimento_ch = element.Ambito_riferimento_ch

    if not pd.isnull(element.Autore_definizione_ch):    
        entry.Autore_definizione_ch = element.Autore_definizione_ch

    if not pd.isnull(element.Posizione_definizione_ch):    
        entry.Posizione_definizione_ch = element.Posizione_definizione_ch

    if not pd.isnull(element.Url_definizione_ch):    
        entry.Url_definizione_ch = element.Url_definizione_ch

    if not pd.isnull(element.Titolo_documento_fonte_ch):    
        entry.Titolo_documento_fonte_ch = element.Titolo_documento_fonte_ch

    if not pd.isnull(element.Autore_documento_fonte_ch):    
        entry.Autore_documento_fonte_ch = element.Autore_documento_fonte_ch

    if not pd.isnull(element.Host_documento_fonte_ch):    
        entry.Host_documento_fonte_ch = element.Host_documento_fonte_ch

    if not pd.isnull(element.Url_documento_fonte):    
        entry.Url_documento_fonte_ch = element.Url_documento_fonte_ch

    if not pd.isnull(element.Commento_entry):    
        entry.Commento_entry=element.Commento_entry

        
    entry.Data_inserimento_entry=element.Data_inserimento_entry
    entry.Id_statico_entry=element.Id_statico_entry               
    entry.Admin_approval_switch=element.Admin_approval_switch

    entry.save()

    print("Riversamento terminato con successo!")


def pour_latest_file():    

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_latest_file!")

    latest_file_element = glossary_file.objects.latest('Data_inserimento_glossary')

    print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % latest_file_element)
  
    excel_sheet = pd.read_excel(latest_file_element.Glossary_file)

    print("*****") 
    print(excel_sheet)
    print("*****")       

    print("Sbobinatura del dataframe in vettori...")        
    
    col_lemma_it = excel_sheet.Lemma_it
    col_acronimo_it = excel_sheet.Acronimo_it
    col_definizione_it = excel_sheet.Definizione_it
    col_ambito_riferimento_it = excel_sheet.Ambito_riferimento_it
    col_autore_definizione_it = excel_sheet.Autore_definizione_it
    col_posizione_definizione_it = excel_sheet.Posizione_definizione_it
    col_url_definizione_it = excel_sheet.Url_definizione_it
    col_titolo_documento_fonte_it = excel_sheet.Titolo_documento_fonte_it
    col_autore_documento_fonte_it = excel_sheet.Autore_documento_fonte_it
    col_host_documento_fonte_it = excel_sheet.Host_documento_fonte_it
    col_url_documento_fonte_it = excel_sheet.Url_documento_fonte_it

    col_lemma_it = excel_sheet.Lemma_it
    col_acronimo_ch = excel_sheet.Acronimo_ch
    col_definizione_ch = excel_sheet.Definizione_ch
    col_ambito_riferimento_ch = excel_sheet.Ambito_riferimento_ch
    col_autore_definizione_ch = excel_sheet.Autore_definizione_ch
    col_posizione_definizione_ch = excel_sheet.Posizione_definizione_ch
    col_url_definizione_ch = excel_sheet.Url_definizione_ch
    col_titolo_documento_fonte_ch = excel_sheet.Titolo_documento_fonte_ch
    col_autore_documento_fonte_ch = excel_sheet.Autore_documento_fonte_ch
    col_host_documento_fonte_ch = excel_sheet.Host_documento_fonte_ch
    col_url_documento_fonte_ch = excel_sheet.Url_documento_fonte_ch


    col_commento_entry = excel_sheet.Commento_entry
    col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
    col_id_statico_entry = excel_sheet.Id_statico_entry
    col_admin_approval_switch = excel_sheet.Admin_approval_switch

    print("Inizia il riversamento di dati dal foglio %s verso il modello acquired_terminology..." % latest_file_element)

    for i in range(len(col_lemma)):

    # assegna i valori agli attributi uno per uno per evitare i NaN
        
        entry = acquired_terminology.objects.create()
        
        if not pd.isnull(element.Lemma_it):
            entry.Lemma_it = element.Lemma_it

        if not pd.isnull(element.Acronimo_it):
            entry.Acronimo_it = element.Acronimo_it

        if not pd.isnull(element.Definizione_it):    
            entry.Definizione_it = element.Definizione_it

        if not pd.isnull(element.Ambito_riferimento_it):    
            entry.Ambito_riferimento_it = element.Ambito_riferimento_it

        if not pd.isnull(element.Autore_definizione_it):    
            entry.Autore_definizione_it = element.Autore_definizione_it

        if not pd.isnull(element.Posizione_definizione_it):    
            entry.Posizione_definizione_it = element.Posizione_definizione_it

        if not pd.isnull(element.Url_definizione_it):    
            entry.Url_definizione_it = element.Url_definizione_it

        if not pd.isnull(element.Titolo_documento_fonte_it):    
            entry.Titolo_documento_fonte_it = element.Titolo_documento_fonte_it

        if not pd.isnull(element.Autore_documento_fonte_it):    
            entry.Autore_documento_fonte_it = element.Autore_documento_fonte_it

        if not pd.isnull(element.Host_documento_fonte_it):    
            entry.Host_documento_fonte_it = element.Host_documento_fonte_it

        if not pd.isnull(element.Url_documento_fonte):    
            entry.Url_documento_fonte_it = element.Url_documento_fonte_it

        if not pd.isnull(element.Lemma_ch):
            entry.Lemma_ch = element.Lemma_ch

        if not pd.isnull(element.Acronimo_ch):
            entry.Acronimo_ch = element.Acronimo_ch

        if not pd.isnull(element.Definizione_ch):    
            entry.Definizione_ch = element.Definizione_ch

        if not pd.isnull(element.Ambito_riferimento_ch):    
            entry.Ambito_riferimento_ch = element.Ambito_riferimento_ch

        if not pd.isnull(element.Autore_definizione_ch):    
            entry.Autore_definizione_ch = element.Autore_definizione_ch

        if not pd.isnull(element.Posizione_definizione_ch):    
            entry.Posizione_definizione_ch = element.Posizione_definizione_ch

        if not pd.isnull(element.Url_definizione_ch):    
            entry.Url_definizione_ch = element.Url_definizione_ch

        if not pd.isnull(element.Titolo_documento_fonte_ch):    
            entry.Titolo_documento_fonte_ch = element.Titolo_documento_fonte_ch

        if not pd.isnull(element.Autore_documento_fonte_ch):    
            entry.Autore_documento_fonte_ch = element.Autore_documento_fonte_ch

        if not pd.isnull(element.Host_documento_fonte_ch):    
            entry.Host_documento_fonte_ch = element.Host_documento_fonte_ch

        if not pd.isnull(element.Url_documento_fonte):    
            entry.Url_documento_fonte_ch = element.Url_documento_fonte_ch

        if not pd.isnull(element.Commento_entry):    
            entry.Commento_entry=element.Commento_entry
            
        entry.Data_inserimento_entry=col_data_inserimento_entry[i]
        entry.Id_statico_entry=col_id_statico_entry[i]               
        entry.Admin_approval_switch=col_admin_approval_switch[i]

        entry.save()


    print("Riversamento dei dati in %s terminato con successo!" % latest_file_element)
    print("*****")


    # per eliminare i glossari lo faccio manualmente (glossary_file)

    # elimina tutti i dati dentro acquired terminoliogy
def erase_acquired_terminology():

    print("Viene richiamato l'algoritmo erase_acquired_terminology!")
    
    acquired_terminology.objects.all().delete()
    print("Eliminati tutti i dati dentro acquired_terminology!")


# elimina tutti i dati dentro acquired terminoliogy
def erase_prepared_terminology():

    print("Viene richiamato l'algoritmo erase_prepared_terminology!")
  
    prepared_terminology.objects.all().delete()
    print("Eliminati tutti i dati dentro prepared_terminology!")

