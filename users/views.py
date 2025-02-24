from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import CustomUser


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

