from django import forms
from .models import Owner
class AddOwnerForm(forms.ModelForm):
    class Meta:
        model=Owner  #you tell for which model you want to create a form
        fields="__all__"  #you tell which fields to include in the form except the auto field bcz it will increment automatically
        exclude={"password"}  #this will exclude any field you want
        labels={"city":"Enter the city","gender":"Select Gender"}  #you can change label name int the form

        