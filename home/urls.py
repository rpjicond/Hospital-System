from django.urls import path
from . import views

urlpatterns = [
    # Aqui você pode definir as URLs específicas para o app 'home'
    path('', views.home_view, name='home'),
]
