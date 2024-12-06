from django.db import models
from django.utils import timezone

# Model para Pacientes
class Patient(models.Model):
    SEX_CHOICES = [('Homme', 'Homme'), ('Femme', 'Femme')]
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ]

    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    sexe = models.CharField(max_length=10, choices=SEX_CHOICES)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    groupe_sanguin = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, blank=True, null=True)
    date_inscription = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.nom} {self.prenom}'


# Model para Trabalhadores (Classe base)
class Travailleur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    date_embauche = models.DateField(auto_now_add=True)
    mot_de_passe = models.CharField(max_length=255)  # Campo para senha

    class Meta:
        abstract = True  # Define esta classe como abstrata (não será criada diretamente no banco de dados)

    def __str__(self):
        return f'{self.nom} {self.prenom}'


# Model para Docteurs (Médicos)
class Docteur(Travailleur):
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nom} {self.prenom} - {self.specialite}'


# Model para Infirmiers (Enfermeiros)
class Infirmier(Travailleur):
    # Aqui podemos adicionar campos específicos dos enfermeiros, se necessário
    pass


# Model para Consultations
class Consultation(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    date_consultation = models.DateField()
    diagnostic = models.TextField(blank=True, null=True)
    traitement_prescrit = models.TextField(blank=True, null=True)
    id_maladie = models.ForeignKey('Maladie', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Consultation {self.id} - Patient: {self.id_patient} - Docteur: {self.id_docteur}'


# Model para Maladies (Doenças)
class Maladie(models.Model):
    nom_maladie = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    symptomes = models.TextField(blank=True, null=True)
    traitement = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom_maladie


# Model para Hospitalisations (Internações)
class Hospitalisation(models.Model):
    STATUT_CHOICES = [('En cours', 'En cours'), ('Terminé', 'Terminé')]

    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_entree = models.DateField()
    date_sortie = models.DateField(blank=True, null=True)
    chambre = models.CharField(max_length=10, blank=True, null=True)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='En cours')

    def __str__(self):
        return f'Hospitalisation {self.id} - Patient: {self.id_patient}'


# Model para Rendez-vous (Consultas Agendadas)
class RendezVous(models.Model):
    id_patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    id_docteur = models.ForeignKey(Docteur, on_delete=models.CASCADE)
    date_rendez_vous = models.DateField()
    heure_rendez_vous = models.TimeField()
    motif = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Rendez-vous {self.id} - Patient: {self.id_patient} - Docteur: {self.id_docteur}'
