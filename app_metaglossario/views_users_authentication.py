from django.shortcuts import render, redirect


# importare i dati degli utenti registrati
from .forms import UserForm
from .forms import UserProfileInfoForm

# per caricare i files dagli utenti
from django.core.files.storage import FileSystemStorage


# per permettere il login
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required
def registration(request):

    registered = False

    # se l'utente ha lanciato il post
    if request.method=="POST":

        print("post eseguito!")
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # condizione di validità del form
        if user_form.is_valid() and profile_form.is_valid():
            
            print("form validi!")

            user = user_form.save()
            user.set_password(user.password) # questa linea hasha la pasword
            user.save()
            # registra l'utente

            profile = profile_form.save(commit=False)
            profile.user = user

            registered=True

            print("Utente registrato con successo!")

            # condizione per registrare l'utente
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                print("Acquisita la fotografia dell'utente!")
            
            profile.save()
            # attenzione al salvataggio dei form e dei modelli che sono due cose diverse
                # registra le info aggiuntive

                

        else:
            print("Registrazione fallita:")
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    context_dict = {'user_form':user_form, 'profile_form':profile_form, 'registered':registered}

    return render(request, 'authentication/registration.html', context_dict)


def user_login(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:

            print("Condizione if user verificata!")

            if user.is_active:

                print("Condizione if user.is_active verificata!")
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

            else:
                HttpResponse("Account non attivo")
        
        else:
            print("qualcuno ha cercato di loggarsi e ha fallito")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Inseriti parametri non validi per il login!")

    else:
        return render(request, "authentication/login.html", {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def special(request):
    return HttpResponse("Sei loggato!")