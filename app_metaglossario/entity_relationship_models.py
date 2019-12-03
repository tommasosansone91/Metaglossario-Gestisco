from django.db import models

# Tabella delle entità


# class model_Things(models.Model): 

#     ID = models.CharField(max_length=10, primary_key=True)
#     Oggetto = models.TextField(blank=True, null=True)

#     class Meta:
#         ordering = ['ID', 'Oggetto']

#     def __str__(self):                
#         return  "[ %s ] : %s"  %  (self.ID, self.Oggetto)


# # Tabelle relazionali
# class model_is_Acronimo_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)


# class model_is_Lemma_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Ambito_riferimento_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Autore_definizione_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Posizione_definizione_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Url_definizione_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)


# class model_is_Titolo_documento_fonte_of(models.Model): 
    
#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)


# class model_is_Autore_documento_fonte_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Host_documento_fonte_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Url_documento_fonte_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Commento_entry_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Data_inserimento_entry_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Id_statico_entry_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



# class model_is_Admin_approval_switch_of(models.Model): 

#     ID_soggetto = models.CharField(max_length=10)
#     ID_oggetto = models.CharField(max_length=10)

#     class Meta:
#         ordering = ['ID_soggetto', 'ID_oggetto']

#     def __str__(self):                
#         return  "[ %s ] <---> [ %s ]"  %  (self.ID_soggetto, self.ID_oggetto)



