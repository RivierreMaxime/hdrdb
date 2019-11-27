from django import forms
from crud.models import Film
import datetime

class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = "__all__"
        titre = forms.CharField(max_length=255)
        annee_sortie = forms.CharField(max_length=255)

        # nom = forms.CharField( max_length=255)
        # prenom = forms.CharField(max_length=255)

        # libelle = forms.CharField(max_length=255)