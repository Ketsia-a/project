from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Profile, Rate
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','bio','profile_pic']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','project_pic','description','link']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['user','project']