from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models.Ppe import Ppe
from .models.Equipment import Equipment
from .models.Material import Material
from .models.Tool import Tool
from .models.Worker import Worker
from .models.Loan import Loan

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
        fields = ['name', 'quantity', 'unitCost', 'stock', 'image']

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
        fields = ['dni', 'name', 'surname', 'position', 'contractDate']
        widgets = {
            'contractDate': forms.DateInput(attrs={'id': 'id_contractDate', 'autocomplete': 'off'}),
        }

class LoanForm(forms.ModelForm):
    ppe = forms.ModelChoiceField(queryset=Ppe.objects.all(), required=False)
    material = forms.ModelChoiceField(queryset=Material.objects.all(), required=False)
    tool = forms.ModelChoiceField(queryset=Tool.objects.all(), required=False)
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=False)
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), required=False)

    class Meta:
        model = Loan
        fields = ['loanDate', 'returnLoanDate', 'worker', 'ppe', 'material', 'tool', 'equipment']

        widgets = {
            'loanDate': forms.DateInput(attrs={'id': 'id_loanDate', 'autocomplete': 'off'}),
            'returnLoanDate': forms.DateInput(attrs={'id': 'id_returnLoanDate', 'autocomplete': 'off'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        worker = cleaned_data.get('worker')
        loan_date = cleaned_data.get('loanDate')
        return_loan_date = cleaned_data.get('returnLoanDate')
    
        if worker and loan_date and return_loan_date:
            # Verificar si hay préstamos existentes para este trabajador en las fechas especificadas
            existing_loans = Loan.objects.filter(
                worker=worker,
                returnLoanDate__gte=loan_date,
                loanDate__lte=return_loan_date,
            ).exclude(pk=self.instance.pk).exists()
            
            if existing_loans:
                raise ValidationError(f'El trabajador ya tiene objetos prestados durante este período.')
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker'].label_from_instance = self.label_from_instance
        self.fields['ppe'].label_from_instance = self.label_from_instance
        self.fields['material'].label_from_instance = self.label_from_instance
        self.fields['tool'].label_from_instance = self.label_from_instance
        self.fields['equipment'].label_from_instance = self.label_from_instance
    
    def label_from_instance(self, obj):
        if isinstance(obj, Worker):
            return f"{obj.name} {obj.surname}"
        else:
            return obj.name