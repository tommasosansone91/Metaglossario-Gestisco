from app_metaglossario.metaglossary_models import *
from app_metaglossario.models import prepared_terminology
# from app_metaglossario.models import displaying_terminology

def algoritmo_WD():

    print("Viene richiamato l'algoritmo WD!")

    # algoritmo per standardizzare i dati prima di incatenarli nella struttura relazionale

    # nota: ci sono dati con lo stesso ID perchè sono i lemmi inglesi eliminati

    import numpy as np
    import pandas as pd