# contiene 2 algoritmi per la gestione del modello dei file-glossari

from app_metaglossario.models import *
import pandas as pd



def pour_entire_file_model():

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_entire_file_model!")

    print("Inizia il riversamento della terminologia di tutti i file salvati nel modello glossary_file verso il modello acquired_terminology...")

    # tutti gli oggetti nel modello glossario sono salvati qui
    all_files = glossary_file.objects.all()
    
    for file_element in all_files: 

        # scansiona, estrai e riversa la terminologia nel file in oggetto solo se l'amministrazione ha impostato che la si può mostrare
        if file_element.Admin_approval_switch == "show":
   
            # per ogni foglio nel modello
            print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % file_element.Glossary_file)
            
            # accedo all'attributo file del modello
            # salva il contenuto del file in una variabile = dataframe
            excel_sheet = pd.read_excel(file_element.Glossary_file)

            print("*****") 
            print(excel_sheet)
            print("*****")       

            print("Sbobinatura del dataframe in vettori...")  

            L_excel_sheet = len(excel_sheet.index)   
            # print(L_excel_sheet) 

                 
            
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

            col_lemma_ch = excel_sheet.Lemma_ch
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

            

                      
                
            # su queste metti colonna automatica
                # la struttura: se esistono, allora fai, la rendo con try+except
            # serve un formato compatibile con il formato che usa per le colonne del dataframe, non sono liste
     

            # autocompila data se non presente colonna aggiunta da admin
            try:
                col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
            except:
                print("L'amministratore di sistema non ha inserito una colonna coi valori di Data_inserimento_entry. Viene aggiunta per default una colonna di valori della data di inserimento del file glossario.")
                
                col_data_inserimento_entry = pd.DataFrame(data=[file_element.Data_inserimento_glossary for i in range(L_excel_sheet)], columns=["Data_inserimento_entry"])


            # autocompila id statici se non presente colonna aggiunta da admin
            try:
                col_id_statico_entry = excel_sheet.Id_statico_entry
            except:
                print("L'amministratore di sistema non ha inserito una colonna coi valori di Id_statico_entry. Viene aggiunta per default una colonna di valori di ID pregenerati basati sul tempo in cui sono stati generati.")
                
                from app_metaglossario.algoritmi_processing.script_ausiliari import return_timestamped_id_vector
                col_id_statico_entry = pd.DataFrame(data=return_timestamped_id_vector(L_excel_sheet), columns=["Id_statico_entry"])
                # il +1 mi evita problemi di non-univocità

                # la dict comprehension potrebbe essere talmente veloce che i timestamp rimangono uguali
                # for i in range(L_excel_sheet-1):
                #     if col_id_statico_entry[i] == col_id_statico_entry[i+1]:
                #         raise("ERRORE: La generazione automatica di ID è talmente veloce che i timestamp risultano uguali. L'amministratore di sistema deve inserire manualmente una colonna 'Id_statico_entry' di Id univoci.")

            # autocompila data se non presente colonna aggiunta da admin
            try:
                col_admin_approval_switch = excel_sheet.Admin_approval_switch
            except:
                print("L'amministratore di sistema non ha inserito una colonna coi valori di Admin_approval_switch. Viene aggiunta per default una colonna di valori 'show'.")
                col_admin_approval_switch = pd.DataFrame(data=["show" for i in range(L_excel_sheet)], columns=["Admin_approval_switch"])

           
           # crea foglio excel virtuale in cui aggiungere le 3 colonne create da zero

            missing_columns_glossary_file = pd.concat([ col_data_inserimento_entry, col_id_statico_entry, col_admin_approval_switch ], axis=1)


            saving_file_name = 'missing_columns_glossary_file.xlsx'

            saving_folder_name = 'saved_dataframes'

            import os
            from django.contrib.staticfiles import finders

            finders.find(saving_folder_name)
            searched_locations = finders.searched_locations
            df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)
            missing_columns_glossary_file.to_excel(df_dir)

            # ora ci sono per forza
            col_data_inserimento_entry = missing_columns_glossary_file.Data_inserimento_entry
            col_id_statico_entry = missing_columns_glossary_file.Id_statico_entry
            col_admin_approval_switch = missing_columns_glossary_file.Admin_approval_switch
            


            print("Inizia il riversamento di dati dal foglio %s al modello acquired_terminology..." % file_element.Glossary_file)


            for i in range(L_excel_sheet):

            # assegna i valori agli attributi uno per uno per evitare i NaN
                

                if col_admin_approval_switch[i] == "show": 
                    
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




# algoritmo attualmente non utilizzato
def pour_latest_file():    

    # questo algoritmo va ottimizzato mettendo i cicli delle etichette delle colonne al posto di richiamare ogni elemento del database con la propria etichetta

    print("Viene richiamato l'algoritmo pour_latest_file!")

    latest_file_element = glossary_file.objects.latest('Data_inserimento_glossary')

    # scansiona, estrai e riversa la terminologia nel file in oggetto solo se l'amministrazione ha impostato che la si può mostrare
    if latest_file_element.Admin_approval_switch == "show":

        print("Inizia la lettura del foglio %s per estrarne la terminologia riga per riga..." % latest_file_element)
    
        excel_sheet = pd.read_excel(latest_file_element.Glossary_file)

        print("*****") 
        print(excel_sheet)
        print("*****")       

        L_excel_sheet = len(excel_sheet.index)

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

        col_lemma_ch = excel_sheet.Lemma_ch
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

        

                    
            
        # su queste metti colonna automatica
            # la struttura: se esistono, allora fai, la rendo con try+except
        # serve un formato compatibile con il formato che usa per le colonne del dataframe, non sono liste
    

        # autocompila data se non presente colonna aggiunta da admin
        try:
            col_data_inserimento_entry = excel_sheet.Data_inserimento_entry
        except:
            print("L'amministratore di sistema non ha inserito una colonna coi valori di Data_inserimento_entry. Viene aggiunta per default una colonna di valori della data di inserimento del file glossario.")
            
            col_data_inserimento_entry = pd.DataFrame(data=[file_element.Data_inserimento_glossary for i in range(L_excel_sheet)], columns=["Data_inserimento_entry"])


        # autocompila id statici se non presente colonna aggiunta da admin
        try:
            col_id_statico_entry = excel_sheet.Id_statico_entry
        except:
            print("L'amministratore di sistema non ha inserito una colonna coi valori di Id_statico_entry. Viene aggiunta per default una colonna di valori di ID pregenerati basati sul tempo in cui sono stati generati.")
            
            from app_metaglossario.algoritmi_processing.script_ausiliari import return_timestamped_id_vector
            col_id_statico_entry = pd.DataFrame(data=return_timestamped_id_vector(L_excel_sheet), columns=["Id_statico_entry"])
            # il +1 mi evita problemi di non-univocità

            # la dict comprehension potrebbe essere talmente veloce che i timestamp rimangono uguali
            # for i in range(L_excel_sheet-1):
            #     if col_id_statico_entry[i] == col_id_statico_entry[i+1]:
            #         raise("ERRORE: La generazione automatica di ID è talmente veloce che i timestamp risultano uguali. L'amministratore di sistema deve inserire manualmente una colonna 'Id_statico_entry' di Id univoci.")

        # autocompila data se non presente colonna aggiunta da admin
        try:
            col_admin_approval_switch = excel_sheet.Admin_approval_switch
        except:
            print("L'amministratore di sistema non ha inserito una colonna coi valori di Admin_approval_switch. Viene aggiunta per default una colonna di valori 'show'.")
            col_admin_approval_switch = pd.DataFrame(data=["show" for i in range(L_excel_sheet)], columns=["Admin_approval_switch"])

        
        # crea foglio excel virtuale in cui aggiungere le 3 colonne create da zero

        missing_columns_glossary_file = pd.concat([ col_data_inserimento_entry, col_id_statico_entry, col_admin_approval_switch ], axis=1)


        saving_file_name = 'missing_columns_glossary_file.xlsx'

        saving_folder_name = 'saved_dataframes'

        import os
        from django.contrib.staticfiles import finders

        finders.find(saving_folder_name)
        searched_locations = finders.searched_locations
        df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)
        missing_columns_glossary_file.to_excel(df_dir)

        # ora ci sono per forza
        col_data_inserimento_entry = missing_columns_glossary_file.Data_inserimento_entry
        col_id_statico_entry = missing_columns_glossary_file.Id_statico_entry
        col_admin_approval_switch = missing_columns_glossary_file.Admin_approval_switch


        print("Inizia il riversamento di dati dal foglio %s verso il modello acquired_terminology..." % latest_file_element)

        for i in range(L_excel_sheet):

        # assegna i valori agli attributi uno per uno per evitare i NaN

            if col_admin_approval_switch[i] == "show": 
                
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


        print("Riversamento dei dati in %s terminato con successo!" % latest_file_element)
        print("*****")

