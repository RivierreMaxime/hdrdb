from django.db import models

# Create your models here.
class Film(models.Model):
    titre = models.CharField(max_length=255)
    annee_sortie = models.DateField(_(""), auto_now=False, auto_now_add=False)
    personnes = models.ManyToManyField(Personne)

class Personne(models.Model):
    nom = models.models.CharField(_(""), max_length=255)
    prenom = models.CharField(_(""), max_length=255)
    type_pers = models.ForeignKey(Type, on_delete=models.CASCADE)

class Type(models.Model):
    libelle = models.CharField(_(""), max_length=255)