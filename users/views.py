from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.mail import EmailMessage
from django.contrib import messages
from .models import CustomUser
from .forms import SignUpForm


def login_user(request):
  if request.method == "POST":
    email = request.POST['email']
    password = request.POST['senha']

    try:
      validate_email(email)
    except ValidationError as e:
      messages.error(
         request,
         f"Informe um endereço de email válido."
      )
      return redirect('login_user')
    

    user = CustomUser.objects.filter(email=email).first()

    if user is None:
        messages.error(request, "E-mail inexistente")
        return redirect('login_user')

    user_auth = authenticate(request, username=email, password=password)

    if user_auth is None:
        messages.error(
          request, 
          "E-mail ou Senha inválidos"
        )
        return redirect('login_user')
    else:
      login(request, user_auth)
        
      messages.success(
        request, 
        "Login realizado com sucesso!"
      )
      return redirect('login_user')
  else:
      return render(request, 'login.html')



def register_user(request):
  if request.method == "POST":
    email = request.POST["email"]
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, "Cadastrado com sucesso!")

        mail = EmailMessage(
           subject="Bem-vindo ao Fidelity Pesquisas!",
           body="Olá! Obrigado por se registrar em nosso site. Estamos felizes em tê-lo conosco.",
           from_email="no-reply@fidelitypesquisas.com.br",
           to=[email],
        )
        mail.send()

        return redirect('login_user')
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})
    
  return render(request, 'register.html', {'form': form})


def logout_user(request):
  logout(request)
  messages.success(request, "Você fez o logout com sucesso!")
  return redirect('login_user')