from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError #serve per far funzionare il "compila almeno un campo del form"



# Create your models here.

#Propongo un modello di tipo "biterminale", o meglio "duetto"

# Il duetto è un brano musicale per due voci soliste, con o senza accompagnamento strumentale.
# Il termine nasce per indicare interpretazioni vocali a due che cantano alternandosi od insieme.

#Fare uno switch che permetta di inserire in modalità standard o avanzata

Admin_approval_switch_choices=[
    ("show","show"), # 1=valore da inserire negli script (=variabile), 2=valore assunto in relatà nel db
    ("hide","hide"),
    ]

class glossary_entry(models.Model):

    # unità linguistiche biterminali

    Lemma_it = models.CharField(max_length=256, blank=True, null=True)
    Lemma_ch = models.CharField(max_length=256, blank=True, null=True)

    Acronimo_it = models.CharField(max_length=25, blank=True, null=True)
    Acronimo_ch = models.CharField(max_length=25, blank=True, null=True)

    #devo inserire per forza un default qui
    # If blank=True then the field will not be required, whereas if it's False the field cannot be blank.
    #This includes the admin and your own custom forms.
    # The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form, you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields, which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').
    Definizione_it = models.TextField(blank=True, null=True) # sostituire con textfield?
    Definizione_ch = models.TextField(blank=True, null=True)

    Ambito_riferimento_it = models.CharField(max_length=256, blank=True, null=True)
    Ambito_riferimento_ch = models.CharField(max_length=256, blank=True, null=True)

    Autore_definizione_it = models.CharField(max_length=256, blank=True, null=True)
    Autore_definizione_ch = models.CharField(max_length=256, blank=True, null=True)

    Posizione_definizione_it = models.CharField(max_length=256, blank=True, null=True)
    Posizione_definizione_ch = models.CharField(max_length=256, blank=True, null=True)

    Url_definizione_it = models.URLField(max_length=400, blank=True, null=True)
    Url_definizione_ch = models.URLField(max_length=400, blank=True, null=True)

    Titolo_documento_fonte_it = models.CharField(max_length=256, blank=True, null=True)
    Titolo_documento_fonte_ch = models.CharField(max_length=256, blank=True, null=True)

    Autore_documento_fonte_it = models.CharField(max_length=256, blank=True, null=True)
    Autore_documento_fonte_ch = models.CharField(max_length=256, blank=True, null=True)

    Host_documento_fonte_it = models.CharField(max_length=256, blank=True, null=True)
    Host_documento_fonte_ch = models.CharField(max_length=256, blank=True, null=True)

    Url_documento_fonte_it = models.URLField(max_length=400, blank=True, null=True)
    Url_documento_fonte_ch = models.URLField(max_length=400, blank=True, null=True)


    # unità linguistiche singole

    Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now().date() )
    # Data_inserimento_entry = models.DateField(blank=False, null=False, default=timezone.now().date)

    Id_statico_entry = models.CharField(max_length=256, blank=False, null=False, default="ITCH00000")

    # switch per far apparire le cose solo se revisionate dall'admin nella sessione del glossario.

    # posso avere solo due scelte per questo switch, le definisco a priori nella root del modulo


    Admin_approval_switch = models.CharField(max_length=30,blank=False, null=False, default=Admin_approval_switch_choices[1], choices=Admin_approval_switch_choices)
    
    # il default nel modello fa comparire il valore selazionato quando creo il contenuto dall'admin 
    # e quando aggiungo l'attributo: viene automaticamente aggiunto a tutti gli elementi del modello

    # choices=Admin_approval_switch_choices


    class Meta:
        ordering = ['Admin_approval_switch', 'Lemma_it', 'Lemma_ch', 'Id_statico_entry']
        # il meno davanti all'attributo uol dire che ordina al contrario
        # '-Admin_approval_switch', 
        # faccio comparire per primi gli hide-> nuovi inseriti


    def clean(self):
        if not (self.Lemma_it or self.Lemma_ch or self.Acronimo_it or self.Acronimo_ch or self.Definizione_it or self.Definizione_ch  or self.Ambito_riferimento_it or self.Ambito_riferimento_ch or self.Autore_definizione_it or self.Autore_definizione_ch or self.Posizione_definizione_it or self.Posizione_definizione_ch or self.Url_definizione_it or self.Url_definizione_ch or self.Titolo_documento_fonte_it or self.Titolo_documento_fonte_ch or self.Autore_documento_fonte_it or self.Autore_documento_fonte_ch or self.Host_documento_fonte_it or self.Host_documento_fonte_ch or self.Url_documento_fonte_it or self.Url_documento_fonte_ch):
            raise ValidationError("Non è stata inserita alcuna terminologia. Compilare almeno un campo del form.")

    def __str__(self):    
        # print("%s is %d years old." % (name, age))    
        return  "%s / %s - %s - [%s]"  %  (self.Lemma_it, self.Lemma_ch, self.Id_statico_entry, self.Admin_approval_switch)  #quello che fa apparire nella sezione admin, attributo che riassume tutti gli altri, quindi una primary key presumibilmente, pouò anche esesere la combinazione degli altri

        #  - %s
        #, self.Admin_approval_switch

