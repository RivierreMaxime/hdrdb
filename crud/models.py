from django.db import models

# Create your models here.
# class Type(models.Model):
#     libelle = models.CharField(max_length=255)


# class Personne(models.Model):
#     nom = models.CharField( max_length=255)
#     prenom = models.CharField(max_length=255)
#     type_pers = models.ForeignKey('Type', on_delete=models.CASCADE)


class Film(models.Model):
    title = models.CharField(max_length=255, null=True)
    release_year = models.CharField(max_length=255, null=True)
    duration = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    director = models.CharField(max_length=255, null=True)
    # personnes = models.ManyToManyField('Personne')

#manage.py loaddata "nom-fixture"
#file: fixtures puis nom-fixture.json