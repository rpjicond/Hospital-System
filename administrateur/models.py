from django.db import models

# Model para Permissions
class Permission(models.Model):
    ROLE_CHOICES = [
        ('Client', 'Client'),
        ('Docteur', 'Docteur'),
        ('Infirmier', 'Infirmier'),
        ('Admin', 'Admin')
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.role


# Model para Utilisateurs (Usuários)
class Utilisateur(models.Model):
    nom_utilisateur = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=Permission.ROLE_CHOICES)
    id_personne = models.IntegerField()  # ID relacionado a pessoa (paciente, doutor, etc.)
    id_permission = models.ForeignKey(Permission, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom_utilisateur
