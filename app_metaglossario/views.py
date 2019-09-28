from django.shortcuts import render, redirect
from .models import glossary_entry
from .forms import glossary_entry_form
from django.contrib import messages # questo mi consente di lanciare i messaggi da una pagina all'altra

# per la ricerca
from django.db.models import Q


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def glossario(request):

    query = request.GET.get('q') #q è variabile risultante dalla query del database
    template = "glossario.html" #il template è sempre lo stesso

    # se la query è stata fatta
    if query:
        
        query = request.GET.get('q') #q è variabile risultante dalla query del database
        selected_entries = glossary_entry.objects.filter(Q(Acronimo__icontains=query)|Q(Ambito_riferimento__icontains=query)|Q(Autore_definizione__icontains=query)|Q(Autore_documento_fonte__icontains=query)|Q(Data_inserimento_entry__icontains=query)|Q(Definizione__icontains=query)|Q(Host_documento_fonte__icontains=query)|Q(Id_statico_entry__icontains=query)|Q(Lemma__icontains=query)|Q(Posizione_definizione__icontains=query)|Q(Titolo_documento_fonte__icontains=query)|Q(Url_definizione__icontains=query)|Q(Url_documento_fonte__icontains=query))
        # context = {'all_entries':selected_entries}
        #return render(request, template, context)
        return render(request, template, {'all_entries':selected_entries})

    # se non è stata fatta nessuna query
    else:

        all_entries = glossary_entry.objects.all #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)
        return render(request, template, {'all_entries':all_entries})


   

def aggiungi_terminologia(request):

    if request.method=='POST': #se si esegue il POST (click del pulsante submit)
        form = glossary_entry_form(request.POST or None) 
        
        # request.POST è il contenuto inserito dagli utenti perchè request è il paramentro in ingresso della funzione

        if form.is_valid(): # funzione che controlla la coerenza dei campi (mail, url, numerico, testo, ecc.)
            form.save()
            insert_attempt_output="corretto"
            messages.success(request, ("Terminologia inserita con successo!\nAttendere la convalida da parte dell\'amministratore.\n Per favore non inserire di nuovo la stessa terminologia"))
            return redirect('aggiungi_terminologia')
            # con redirect non posso usare .html, ma per forza names
        else:
            insert_attempt_output="errato"
            messages.error(request, ('ERRORE: La terminologia non è stata inserita nel glossario.\nVerificare se sia stata inserita la data.'))
            return render(request, 'aggiungi_terminologia.html', {'insert_attempt_output':insert_attempt_output})

    else:   # se si va sulla pagina e basta
        return render(request, 'aggiungi_terminologia.html', {}) 




# def vista_ricerca_semplice(request):

#     template = "glossario.html"

#     query = request.GET.get('q') #q è variabile risultante dalla query del database

#     selected_entries = glossary_entry.objects.filter(Q(Lemma_it__icontains=query))

#     context = {'selected_entries':selected_entries}

#     #return render(request, template, context)
#     return render(request, 'glossario.html', {'selected_entries':selected_entries})



