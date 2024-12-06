# administrateur/urls.py

from django.urls import path
from . import views  # Certifique-se de que você tem as views configuradas

urlpatterns = [
    # Supondo que você tenha uma view chamada 'dashboard', por exemplo:
    path('', views.dashboard, name='dashboard'),
]
