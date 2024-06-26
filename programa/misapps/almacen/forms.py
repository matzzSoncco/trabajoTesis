from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models.Ppe import Ppe
from .models.PpeLoan import PpeLoan
from .models.Equipment import Equipment
from .models.Material import Material
from .models.Tool import Tool
from .models.Worker import Worker
from .models.Loan import Loan

class AdminSignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text="Requerido.", label="Nombre de usuario")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  # Hacer que este usuario sea un administrador
        if commit:
            user.save()
        return user

class PpeForm(forms.ModelForm):
    class Meta:
        model = Ppe
        fields = ['name', 'quantity', 'unitCost', 'stock', 'unit', 'guideNumber', 'image']

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'quantity', 'level', 'stock', 'guideNumber']

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['name', 'quantity', 'stock', 'unit', 'guideNumber']

class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['name', 'quantity', 'level', 'stock', 'guideNumber']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['dni', 'name', 'surname', 'position', 'contractDate', 'status']
        widgets = {
            'contractDate': forms.DateInput(attrs={'id': 'id_contractDate', 'autocomplete': 'off'}),
            'status': forms.CheckboxInput(attrs={'class': 'status-checkbox'}),
        }

class LoanForm(forms.ModelForm):
    material = forms.ModelChoiceField(queryset=Material.objects.all(), required=True)
    tool = forms.ModelChoiceField(queryset=Tool.objects.all(), required=True)
    equipment = forms.ModelChoiceField(queryset=Equipment.objects.all(), required=True)
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), required=True)

    class Meta:
        model = Loan
        fields = ['loanDate', 'returnLoanDate', 'worker', 'material', 'tool', 'equipment', 'workOrderCode']

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
                returnLoanDate__gte=return_loan_date,
                loanDate__lte=loan_date,
            ).exclude(pk=self.instance.pk).exists()
            
            if existing_loans:
                raise ValidationError(f'El trabajador ya tiene objetos prestados durante este período.')
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker'].label_from_instance = self.label_from_instance
        self.fields['material'].label_from_instance = self.label_from_instance
        self.fields['tool'].label_from_instance = self.label_from_instance
        self.fields['equipment'].label_from_instance = self.label_from_instance
    
    def label_from_instance(self, obj):
        if isinstance(obj, Worker):
            return f"{obj.name} {obj.surname}"
        else:
            return obj.name
        
class PpeLoanForm(forms.ModelForm):
    ppe = forms.ModelChoiceField(queryset=Ppe.objects.all(), required=True)
    worker = forms.ModelChoiceField(queryset=Worker.objects.all(), required=True)

    class Meta:
        model = PpeLoan
        fields = ['loanDate', 'newLoanDate', 'worker', 'ppe']

        widgets = {
            'loanDate': forms.DateInput(attrs={'id': 'id_loanDate', 'autocomplete': 'off'}),
            'newLoanDate': forms.DateInput(attrs={'id': 'id_newLoanDate', 'autocomplete': 'off'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        worker = cleaned_data.get('worker')
        loan_date = cleaned_data.get('loanDate')
        new_loan_date = cleaned_data.get('newLoanDate')
    
        if worker and loan_date and new_loan_date:
            # Verificar si hay préstamos existentes para este trabajador en las fechas especificadas
            existing_ppe_loans = PpeLoan.objects.filter(
                worker=worker,
                loanDate__lte=new_loan_date,
                newLoanDate__gte=loan_date 
            ).exclude(pk=self.instance.pk).exists()
            
            if existing_ppe_loans:
                raise ValidationError(f'El trabajador ya tiene EPPs entregados durante este período.')
        
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['worker'].label_from_instance = self.label_from_instance
        self.fields['ppe'].label_from_instance = self.label_from_instance
    
    def label_from_instance(self, obj):
        if isinstance(obj, Worker):
            return f"{obj.name} {obj.surname}"
        else:
            return obj.name