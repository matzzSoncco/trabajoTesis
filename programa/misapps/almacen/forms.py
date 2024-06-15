from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models.Ppe import Ppe
from .models.Equipment import Equipment
from .models.Material import Material
from .models.Tool import Tool
from .models.Worker import Worker

class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_staff = True  # Hacer que este usuario sea un administrador
        if commit:
            user.save()
        return user

class PpeForm(forms.ModelForm):
    class Meta:
        model = Ppe
        fields = ['name', 'quantity', 'unitCost', 'stock']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'quantity', 'level', 'stock']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity', 'stock']

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'quantity', 'level', 'stock']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'surname']