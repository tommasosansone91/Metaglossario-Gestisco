from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError #serve per far funzionare il "compila almeno un campo del form"



# Create your models here.

# glossary_entry, glossary_file, acquired_terminology, prepared_terminology

# Fare uno switch che permetta di inserire in modalità standard o avanzata
# queste sono gli unici valori che puo assumere
# implementerò un dropdown menu nella sezione admin
Admin_approval_switch_choices=[
    ("show","show"), # 1=valore da inserire negli script (=variabile), 2=valore assunto in relatà nel db
    ("hide","hide"),
    ]


class glossary_entry(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

    ### unità linguistiche ###
    # 11 linguistiche + data, id, + switch admin 14 in totale

    # parte italiana

    Lemma_it = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_it = models.CharField(max_length=25, blank=True, null=True)

    Definizione_it = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_it = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_it = models.TextField(blank=True, null=True)
    
    Posizione_definizione_it = models.TextField(blank=True, null=True)
    
    Url_definizione_it = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_it = models.URLField(max_length=400, blank=True, null=True)


    # parte italiana

    Lemma_ch = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_ch = models.CharField(max_length=25, blank=True, null=True)

    Definizione_ch = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_ch = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_ch = models.TextField(blank=True, null=True)
    
    Posizione_definizione_ch = models.TextField(blank=True, null=True)
    
    Url_definizione_ch = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_ch = models.URLField(max_length=400, blank=True, null=True)

    

    #### data e ID ####

    # default è un attributo che mi fa apparire quel valore di default nella sezione admin,
    # o meglio nel modello, quando creo un elemento.
    # poi ovviamente lo vedo subito nella sezione admin

    # il default nel modello fa comparire il valore selazionato quando creo il contenuto dall'admin 
    # e quando aggiungo l'attributo: viene automaticamente aggiunto a tutti gli elementi del modello

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now)

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")


    # switch per far apparire le cose solo se revisionate dall'admin nella sessione del glossario.
    # posso avere solo due scelte per questo switch, le definisco a priori nella root del modulo

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)



    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Lemma_it or self.Acronimo_it or self.Definizione_it or  self.Ambito_riferimento_it or self.Autore_definizione_it or self.Posizione_definizione_it or self.Url_definizione_it or self.Titolo_documento_fonte_it or self.Autore_documento_fonte_it or self.Host_documento_fonte_it or self.Url_documento_fonte_it or self.Lemma_ch or self.Acronimo_ch or self.Definizione_ch or  self.Ambito_riferimento_ch or self.Autore_definizione_ch or self.Posizione_definizione_ch or self.Url_definizione_ch or self.Titolo_documento_fonte_ch or self.Autore_documento_fonte_ch or self.Host_documento_fonte_ch or self.Url_documento_fonte_ch or self.Commento_entry):
            raise ValidationError("Non è stata inserita alcuna terminologia. Compilare almeno un campo del form.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s - %s ----- [%s] - [%s] - [%s]"  %  (self.Lemma_it, self.Lemma_ch, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri




class glossary_file(models.Model):

    Glossary_file = models.FileField(upload_to='uploaded_glossaries/', blank=False, null=False)

    Data_inserimento_glossary = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now().date)


    class Meta:
        ordering = ['Data_inserimento_glossary', 'Glossary_file']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Glossary_file_it or self.Data_inserimento_glossary):
            raise ValidationError("Non è stato selezionato alcun glossario per il caricamento.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s ----- [%s]"  %  (self.Glossary_file, self.Data_inserimento_glossary)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri


# qui devo riversare la terminologia contenuta in glossary_entry e glossary_file
class acquired_terminology(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

    ### unità linguistiche ###
    # 11 linguistiche + data, id, + switch admin 14 in totale

    # parte italiana

    Lemma_it = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_it = models.CharField(max_length=25, blank=True, null=True)

    Definizione_it = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_it = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_it = models.TextField(blank=True, null=True)
    
    Posizione_definizione_it = models.TextField(blank=True, null=True)
    
    Url_definizione_it = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_it = models.URLField(max_length=400, blank=True, null=True)


    # parte italiana

    Lemma_ch = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_ch = models.CharField(max_length=25, blank=True, null=True)

    Definizione_ch = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_ch = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_ch = models.TextField(blank=True, null=True)
    
    Posizione_definizione_ch = models.TextField(blank=True, null=True)
    
    Url_definizione_ch = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_ch = models.URLField(max_length=400, blank=True, null=True)

    

    #### data e ID ####

    # default è un attributo che mi fa apparire quel valore di default nella sezione admin,
    # o meglio nel modello, quando creo un elemento.
    # poi ovviamente lo vedo subito nella sezione admin

    # il default nel modello fa comparire il valore selazionato quando creo il contenuto dall'admin 
    # e quando aggiungo l'attributo: viene automaticamente aggiunto a tutti gli elementi del modello

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now)

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")


    # switch per far apparire le cose solo se revisionate dall'admin nella sessione del glossario.
    # posso avere solo due scelte per questo switch, le definisco a priori nella root del modulo

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)



    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Lemma_it or self.Acronimo_it or self.Definizione_it or  self.Ambito_riferimento_it or self.Autore_definizione_it or self.Posizione_definizione_it or self.Url_definizione_it or self.Titolo_documento_fonte_it or self.Autore_documento_fonte_it or self.Host_documento_fonte_it or self.Url_documento_fonte_it or self.Lemma_ch or self.Acronimo_ch or self.Definizione_ch or  self.Ambito_riferimento_ch or self.Autore_definizione_ch or self.Posizione_definizione_ch or self.Url_definizione_ch or self.Titolo_documento_fonte_ch or self.Autore_documento_fonte_ch or self.Host_documento_fonte_ch or self.Url_documento_fonte_ch or self.Commento_entry):
            raise ValidationError("Non è stata inserita alcuna terminologia. Compilare almeno un campo del form.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s - %s ----- [%s] - [%s] - [%s]"  %  (self.Lemma_it, self.Lemma_ch, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri





class prepared_terminology(models.Model):

    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').

        ### unità linguistiche ###
    # 11 linguistiche + data, id, + switch admin 14 in totale

    # parte italiana

    Lemma_it = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_it = models.CharField(max_length=25, blank=True, null=True)

    Definizione_it = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_it = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_it = models.TextField(blank=True, null=True)
    
    Posizione_definizione_it = models.TextField(blank=True, null=True)
    
    Url_definizione_it = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_it = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_it = models.URLField(max_length=400, blank=True, null=True)


    # parte italiana

    Lemma_ch = models.CharField(max_length=256, blank=True, null=True)
    
    Acronimo_ch = models.CharField(max_length=25, blank=True, null=True)

    Definizione_ch = models.TextField(blank=True, null=True) # sostituire con textfield?
    
    Ambito_riferimento_ch = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_ch = models.TextField(blank=True, null=True)
    
    Posizione_definizione_ch = models.TextField(blank=True, null=True)
    
    Url_definizione_ch = models.URLField(max_length=400, blank=True, null=True)
    
    Titolo_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Autore_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Host_documento_fonte_ch = models.TextField(blank=True, null=True)
    
    Url_documento_fonte_ch = models.URLField(max_length=400, blank=True, null=True)

    

    #### data e ID ####

    # default è un attributo che mi fa apparire quel valore di default nella sezione admin,
    # o meglio nel modello, quando creo un elemento.
    # poi ovviamente lo vedo subito nella sezione admin

    # il default nel modello fa comparire il valore selazionato quando creo il contenuto dall'admin 
    # e quando aggiungo l'attributo: viene automaticamente aggiunto a tutti gli elementi del modello

    Commento_entry = models.TextField(blank=True, null=True)

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now)

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")


    # switch per far apparire le cose solo se revisionate dall'admin nella sessione del glossario.
    # posso avere solo due scelte per questo switch, le definisco a priori nella root del modulo

    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)



    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Data_inserimento_entry', 'Id_statico_entry']
        # il meno davanti all'attributo vuol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti
        # in realtà per come ho definito hide e show, se metto senza il meno davanti, mi mostra per prima hide (h viene prima di s)

    def clean(self):
        if not (self.Lemma_it or self.Acronimo_it or self.Definizione_it or  self.Ambito_riferimento_it or self.Autore_definizione_it or self.Posizione_definizione_it or self.Url_definizione_it or self.Titolo_documento_fonte_it or self.Autore_documento_fonte_it or self.Host_documento_fonte_it or self.Url_documento_fonte_it or self.Lemma_ch or self.Acronimo_ch or self.Definizione_ch or  self.Ambito_riferimento_ch or self.Autore_definizione_ch or self.Posizione_definizione_ch or self.Url_definizione_ch or self.Titolo_documento_fonte_ch or self.Autore_documento_fonte_ch or self.Host_documento_fonte_ch or self.Url_documento_fonte_ch or self.Commento_entry):
            raise ValidationError("Non è stata inserita alcuna terminologia. Compilare almeno un campo del form.")
        # non mi restituisce questa scritta ma quella messa di default nelle views

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s - %s ----- [%s] - [%s] - [%s]"  %  (self.Lemma_it, self.Lemma_ch, self.Id_statico_entry, self.Data_inserimento_entry, self.Admin_approval_switch)  
        #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri