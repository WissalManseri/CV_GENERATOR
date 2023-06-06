from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Document(models.Model):
    photo = models.ImageField(upload_to="photo_profile")
    nom = models.CharField(max_length=100,verbose_name="nom de famille")
    prenom = models.CharField(max_length=50,verbose_name="votre prenom")
    date = models.DateField(verbose_name="date de naissance")
    lieu = models.CharField(max_length=100,verbose_name="lieu de naissance")
    email = models.EmailField(verbose_name="votre email")
    phonenumber = PhoneNumberField(verbose_name="contacte",unique=False)