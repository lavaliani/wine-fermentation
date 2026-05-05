from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import FermentationEntry, WineProject


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="ელ-ფოსტა")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        labels = {"username": "მომხმარებელი"}


class GeorgianAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label="მომხმარებელი")
    password = forms.CharField(label="პაროლი", widget=forms.PasswordInput)


class WineProjectForm(forms.ModelForm):
    class Meta:
        model = WineProject
        fields = [
            "name",
            "grape_type",
            "harvest_date",
            "wine_style",
            "initial_brix",
            "initial_sugar",
            "initial_ph",
            "initial_acidity",
            "vessel",
            "volume_liters",
            "notes",
            "is_active",
        ]
        widgets = {"harvest_date": forms.DateInput(attrs={"type": "date"}), "notes": forms.Textarea(attrs={"rows": 4})}


class FermentationEntryForm(forms.ModelForm):
    class Meta:
        model = FermentationEntry
        fields = ["measured_at", "temperature", "brix", "sugar", "ph", "acidity", "action", "comment"]
        widgets = {"measured_at": forms.DateTimeInput(attrs={"type": "datetime-local"}), "comment": forms.Textarea(attrs={"rows": 3})}
