from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL do painel de administração padrão do Django
    path('admin/', admin.site.urls),

    # URL da aplicação 'home'
    path('', include('home.urls')),

    # URL da aplicação 'authentication' com o namespace 'auth'
    path('auth/', include('authentication.urls', namespace='auth')),

    # URL para o painel administrativo do app 'administrateur'
    path('admin2/', include('administrateur.urls')),
]
