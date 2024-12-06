from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

# Requer que o usuário esteja logado para acessar a página inicial
@login_required(login_url='auth:login')
def home_view(request):  # Renomeie para home_view
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
