from django import forms
from .models import Document
from phonenumber_field.modelfields import PhoneNumberField



class DocumentForm(forms.ModelForm):
    college = forms.CharField(max_length=100,required=False)
    lycee = forms.CharField(max_length=100,required=False)
    universite_institut_ecole = forms.CharField(max_length=100,required=False) 
    niveau_d_etude = forms.CharField(max_length=80,required=False)
    information = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'quelque information a savoir sur vous'}),required=False)
    ancien_Poste = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'parlez de vos ancien poste'}),required=False)

    class Meta:
        model = Document
        fields = [
            'photo','nom','prenom','date','lieu','email','phonenumber',
            'college','lycee','universite_institut_ecole','niveau_d_etude','information','ancien_Poste']