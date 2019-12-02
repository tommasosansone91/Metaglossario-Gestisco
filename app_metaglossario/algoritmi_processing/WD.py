from app_metaglossario.metaglossary_models import *
from app_metaglossario.node_models import *
from app_metaglossario.models import displaying_terminology

# script prova
from django.contrib.staticfiles.templatetags.staticfiles import static
url = static('x.jpg')

# deve essere richiamato dall'algoritmo SR altrimenti ci mette troppo tempo

def algoritmo_WD():

    print("Viene richiamato l'algoritmo WD!")

    # algoritmo per organizzare i dati per la visualizzazione
    # la chiave è costruire una vista che permette di vedere un oggetto alla volta, 
    # col punto di vista incentrato su quell'oggetto, circondato dai related.

    # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

    import numpy as np
    import pandas as pd

    import os    
    from django.contrib.staticfiles import finders

    saving_folder_name = 'saved_dataframes'

    saving_file_name = 'output_table.xlsx'

    result = finders.find(saving_folder_name)
    searched_locations = finders.searched_locations

    df_dir = os.path.join(searched_locations[0]+r'\\'+saving_folder_name+r'\\'+saving_file_name)

    df1 = pd.DataFrame([['a', 'b'], ['c', 'd']])
    df1.to_excel(df_dir)

    # importa la tabella excel Elab 1 e salvala come dataframe
    # usala per riempire il modello node, seguendo la struttura relazionale del mtaglossario
    # aggiungi commento entri e admin approval switch


    
    # model_node.objects.all().delete()
    # print("Eliminati tutti i dati dentro model_node!")

  





