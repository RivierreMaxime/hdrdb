from django.db import models

# Create your models here.
# class Type(models.Model):
#     libelle = models.CharField(max_length=255)


# class Personne(models.Model):
#     nom = models.CharField( max_length=255)
#     prenom = models.CharField(max_length=255)
#     type_pers = models.ForeignKey('Type', on_delete=models.CASCADE)


class Film(models.Model):
    titre = models.CharField(max_length=255)
    annee_sortie = models.CharField(max_length=255)
    # personnes = models.ManyToManyField('Personne')

#manage.py loaddata "nom-fixture"
#file: fixtures puis nom-fixture.json