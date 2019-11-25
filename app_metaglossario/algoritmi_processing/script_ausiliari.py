import sys
import time
import winsound


def printout():

    print("Script richiamato con successo!")
    start_time = time.time()
    return start_time


def printout_input(input):

    start_time = time.time()
    script_name = "Script di conferma"
    print("%s richiamato con successo con il seguente input: %s" % (script_name, input))
    
    return start_time


def finish_sound():
    
    duration = 150  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)
