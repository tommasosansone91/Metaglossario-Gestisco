# contiene due algoritmi per cancellare il contenuto dei modelli ove viene processata la erminologia

from app_metaglossario.models import *
import pandas as pd



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


# per eliminare i glossari lo faccio manualmente (glossary_file)

#algoritmi di emergenza per eliminare i contenuti da backend:
def erase_glossary_entry():

    print("Viene richiamato l'algoritmo erase_glossary_entry!")
  
    glossary_entry.objects.all().delete()
    print("Eliminati tutti i dati dentro glossary_entry!")


def erase_glossary_file():

    print("Viene richiamato l'algoritmo erase_glossary_file!")
  
    glossary_file.objects.all().delete()
    print("Eliminati tutti i dati dentro glossary_file!")