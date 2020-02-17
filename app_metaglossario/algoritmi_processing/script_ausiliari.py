import sys
import time


def return_timestamped_id():

    prefisso = "ITCH"
    
    import time

    adesso = time.time()
    adesso = adesso*10000000
    adesso = int(adesso)

    timestamp = str(adesso)

    valore_default = prefisso + timestamp

    return(valore_default)




def return_timestamped_id_vector(L_vector):

    prefisso = "ITCH"
    
    import time

    adesso = time.time()
    adesso = adesso*10000000
    adesso = int(adesso)

    orario_adulterato = adesso
    vettore_valori_default = []

    for i in range (L_vector):

        orario_adulterato = orario_adulterato + 1

        timestamp = str(orario_adulterato)

        valore_default = prefisso + timestamp

        vettore_valori_default.append(valore_default)
        # le liste sono immutabili

    return(vettore_valori_default)



def finish_sound():
    
    # import winsound
    # duration = 150  # milliseconds
    # freq = 440  # Hz
    # winsound.Beep(freq, duration)
    # winsound.Beep(freq, duration)
    # winsound.Beep(freq, duration)

    from playsound import playsound
    # import os    

    # from django.contrib.staticfiles import finders

    # result = finders.find('static/sounds/1607.mp3')
    # searched_locations = finders.searched_locations

    # # print(searched_locations[0])
    # # print(os.path.join(searched_locations[0]+r'\sounds\1607.mp3'))

    # sound_dir = os.path.join(searched_locations[0]+r'\sounds\1607.mp3')

    # playsound(sound_dir)

    # print("(Suono di fine script eseguito!)")
