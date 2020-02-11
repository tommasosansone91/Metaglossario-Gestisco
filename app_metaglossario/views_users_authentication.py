from django.shortcuts import render, redirect


# importare i dati degli utenti registrati
from .forms import UserForm
from .forms import UserProfileInfoForm

# per caricare i files dagli utenti
from django.core.files.storage import FileSystemStorage


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