from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home:home')  # Se o usuário já estiver logado, redireciona para a home
    
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        username = form.cleaned_data.get('username') if form.is_valid() else None  # Obtém o nome de usuário, se o formulário for válido
        print(f"Tentativa de connexion pour l'utilisateur: {username}")  # Mostra o usuário tentando logar
        
        if form.is_valid():
            password = form.cleaned_data.get('password')
            print(f"Mot de passe tenté: {password}")  # (Opcional) Imprime a senha tentada
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print(f"Utilisateur '{username}' connecté avec succès!")  # Usuário autenticado
                login(request, user)
                return redirect('home:home')
            else:
                print(f"Échec de la connexion pour l'utilisateur '{username}' : mot de passe incorrect.")  # Senha incorreta
        else:
            print("Formulaire invalide.")
            #print("Erreurs du formulaire:", form.errors)

    return render(request, 'index.html', {'form': form})

def logout_view(request):
    print(f"L'utilisateur {request.user.username} s'est déconnecté.")  # Exibe o nome do usuário que está fazendo logout
    logout(request)
    return redirect('auth:login')  # Redireciona para a página de login após o logout
