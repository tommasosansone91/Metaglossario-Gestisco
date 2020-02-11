from django.db import models

# PER LA CREAZIONE DEI PROFILI UTENTI
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    # relazione (serve a permettere l'estensione dei dati associati all'utente)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    # altri attributi
    profile_pic = models.ImageField(blank=True, null=True, upload_to="profile_pics")
    user_link = models.URLField(blank=True, null=True)
    # user_bio = models.TextField(blank=True)

    def __str__(self):
        # built-in  attribute of django.contrib.auth.models.User
        return self.user.username