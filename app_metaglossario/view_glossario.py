from django.shortcuts import render, redirect

# per la ricerca
from django.db.models import Q

# per la paginazione
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage, PageNotAnInteger

from .models import prepared_terminology


def glossario(request):   

    query = request.GET.get('q') #q è variabile risultante dalla query del database
    # non sostuituirla col valore vuoto

    template = "glossario.html" #il template è sempre lo stesso

    all_entries = prepared_terminology.objects.all() #funziona lo stesso anche se dice Class 'glossary_entry' has no 'objects' memberpylint(no-member)

    # se la query è stata fatta, query contiene il termine inserito dall'utente
    if query:

        query = request.GET.get('q') #q è variabile risultante dalla query del database

        #filtro intelligente: 
        if query.lower().startswith("acronimo:"):
            query = query[9:]
            print("Ricerca '%s' tra gli acronimi" % query)
            selected_entries = prepared_terminology.objects.filter(Q(Acronimo_it__icontains=query)|Q(Acronimo_ch__icontains=query))

        #filtro intelligente: 
        elif query.lower().startswith("lemma:"):
            query = query[6:]
            print("Ricerca '%s' tra i lemmi" % query)
            selected_entries = prepared_terminology.objects.filter(Q(Lemma_it__icontains=query)|Q(Lemma_ch__icontains=query))

        #filtro intelligente: 
        elif query.lower().startswith("definizione:"):
            query = query[12:]
            print("Ricerca '%s' tra le definizioni" % query)
            selected_entries = prepared_terminology.objects.filter(Q(Definizione_it__icontains=query)|Q(Definizione_ch__icontains=query))

        #filtro intelligente: 
        elif query.lower().startswith("fonte:"):
            query = query[6:]
            print("Ricerca '%s' tra gli autori di definizioni e di documenti fonte, tra i titoli dei documenti fonte e tra gli host dei documenti fonte." % query)
            selected_entries = prepared_terminology.objects.filter(Q(Autore_definizione_it__icontains=query)|Q(Autore_documento_fonte_it__icontains=query)|Q(Host_documento_fonte_it__icontains=query)|Q(Titolo_documento_fonte_it__icontains=query)|Q(Autore_definizione_ch__icontains=query)|Q(Autore_documento_fonte_ch__icontains=query)|Q(Host_documento_fonte_ch__icontains=query)|Q(Titolo_documento_fonte_ch__icontains=query)    )

        elif query.lower().startswith("url:"):
            query = query[4:]
            print("Ricerca '%s' gli URL" % query)
            selected_entries = prepared_terminology.objects.filter(Q(Url_documento_fonte_it__icontains=query)|Q(Url_documento_fonte_ch__icontains=query))


        else:        
            print("Ricerca '%s' in tutti i campi" % query)
            selected_entries = prepared_terminology.objects.filter(Q(Acronimo_it__icontains=query)|Q(Ambito_riferimento_it__icontains=query)|Q(Autore_definizione_it__icontains=query)|Q(Autore_documento_fonte_it__icontains=query)|Q(Definizione_it__icontains=query)|Q(Host_documento_fonte_it__icontains=query)|Q(Lemma_it__icontains=query)|Q(Posizione_definizione_it__icontains=query)|Q(Titolo_documento_fonte_it__icontains=query)|Q(Url_definizione_it__icontains=query)|Q(Url_documento_fonte_it__icontains=query)|Q(Acronimo_ch__icontains=query)|Q(Ambito_riferimento_ch__icontains=query)|Q(Autore_definizione_ch__icontains=query)|Q(Autore_documento_fonte_ch__icontains=query)|Q(Definizione_ch__icontains=query)|Q(Host_documento_fonte_ch__icontains=query)|Q(Lemma_ch__icontains=query)|Q(Posizione_definizione_ch__icontains=query)|Q(Titolo_documento_fonte_ch__icontains=query)|Q(Url_definizione_ch__icontains=query)|Q(Url_documento_fonte_ch__icontains=query)| Q(Data_inserimento_entry__icontains=query)| Q(Id_statico_entry__icontains=query))
            # Q(Acronimo__icontains=query dice quali sono i campi in cui cercare l'input specificato dall'utente

        # Pagination
        paginator = Paginator(selected_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        selected_entries = paginator.get_page(page)

        # context = {'all_entries':selected_entries}
        #return render(request, template, context)
        # {'nome della variabile con cui sarà richiamato nel template':contenuto}
        return render(request, template, {'all_entries':selected_entries, 'query':query})

    # se non è stata fatta nessuna query
    else:

        # Pagination
        paginator = Paginator(all_entries, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        all_entries = paginator.get_page(page)

        return render(request, template, {'all_entries':all_entries, 'query':query})