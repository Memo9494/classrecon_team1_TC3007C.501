from django import forms
from django.forms import ModelForm, BaseModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Attendance, Participation, Course

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = {'username','first_name','last_name','email','age','degree','semester','photo'}

    
class CustomUserChangeForm(ModelForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = {'username','first_name','last_name','email','age','degree','semester','courses','is_staff','is_superuser','photo','face_encoding'}
        widgets = {'courses': forms.CheckboxSelectMultiple(),'photo': forms.FileInput()}
