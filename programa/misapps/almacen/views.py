from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models.Ppe import Ppe
from .models.PpeLoan import PpeLoan
from .models.Equipment import Equipment
from .models.Worker import Worker
from .models.Material import Material
from .models.Loan import Loan
from .models.Tool import Tool
from .forms import AdminSignUpForm, PpeForm, MaterialForm, WorkerForm, EquipmentForm, ToolForm, LoanForm, PpeLoanForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

#PPE
def PersonalProtectionEquipment(request):
    query = request.GET.get('q')
    if query:
        epp = Ppe.objects.filter(name__icontains=query)
    else:
        epp = Ppe.objects.all()
    return render(request, 'ppe.html', {'epp': epp, 'query': query})

def add_ppe(request):
    if request.method == 'POST':
        form = PpeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ppe')
    else:
        form = PpeForm()
    return render(request, 'add_ppe.html', {'form': form})

def delete_ppe(request, id):
    epp = get_object_or_404(Ppe, idPpe=id)
    
    if request.method == 'POST':
        epp.delete()
        return redirect('ppe')
    else:
        return render(request, 'delete_ppe.html', {'epp': epp})
    
def modify_ppe(request, id):
    epp = get_object_or_404(Ppe, idPpe=id)
    form = PpeForm(instance=epp)

    if request.method == 'POST':
        form = PpeForm(request.POST, instance=epp)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('ppe')
    else:
        return render(request, 'modify_ppe.html', {'form': form})

#EQUIMENT
def equipment_list(request):
    query = request.GET.get('q')
    if query:
        equipment = Equipment.objects.filter(name__icontains=query)
    else:
        equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment, 'query': query})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'add_equipment.html', {'form': form})

def delete_equipment(request, id):
    equipment = get_object_or_404(Equipment, idEquipment=id)
    
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    else:
        return render(request, 'delete_ppe.html', {'equipment': equipment})
    
def modify_equipment(request, id):
    equipment = get_object_or_404(Equipment, idEquipment=id)
    form = EquipmentForm(instance=equipment)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('equipment_list')
    else:
        return render(request, 'modify_equipment.html', {'form': form})

#MATERIAL
def material_list(request):
    query = request.GET.get('q')
    if query:
        materials = Material.objects.filter(name__icontains=query)
    else:
        materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials, 'query': query})

def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'add_material.html', {'form': form})

def delete_material(request, id):
    material = get_object_or_404(Material, idMaterial=id)
    
    if request.method == 'POST':
        material.delete()
        return redirect('material_list')
    else:
        return render(request, 'delete_material.html', {'material': material})
    
def modify_material(request, id):
    material = get_object_or_404(Material, idMaterial=id)
    form = MaterialForm(instance=material)

    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('material_list')
    else:
        return render(request, 'modify_material.html', {'form': form})

#TOOLS
def tool_list(request):
    query = request.GET.get('q')
    if query:
        tools = Tool.objects.filter(name__icontains=query)
    else:
        tools = Tool.objects.all()
    return render(request, 'tool_list.html', {'tools': tools, 'query': query})

def add_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tool_list')
    else:
        form = ToolForm()
    return render(request, 'add_tool.html', {'form': form})

def delete_tool(request, id):
    tools = get_object_or_404(Tool, idTool=id)
    
    if request.method == 'POST':
        tools.delete()
        return redirect('tool_list')
    else:
        return render(request, 'delete_ppe.html', {'tools': tools})
    
def modify_tool(request, id):
    tools = get_object_or_404(Tool, idTool=id)
    form = ToolForm(instance=tools)

    if request.method == 'POST':
        form = ToolForm(request.POST, instance=tools)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('tool_list')
    else:
        return render(request, 'modify_tool.html', {'form': form})

#WORKER
def worker_list(request):
    query = request.GET.get('q')
    if query:
        workers = Worker.objects.filter(worker__name__icontains=query)
    else:
        workers = Worker.objects.all()
    return render(request, 'worker_list.html', {'workers': workers, 'query': query})

def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'add_worker.html', {'form': form})

def delete_worker(request, id):
    workers = get_object_or_404(Worker, dni=id)
    
    if request.method == 'POST':
        workers.delete()
        return redirect('worker_list')
    else:
        return render(request, 'delete_worker.html', {'workers': workers})
    
def modify_worker(request, id):
    workers = get_object_or_404(Worker, dni=id)
    form = WorkerForm(instance=workers)

    if request.method == 'POST':
        form = WorkerForm(request.POST, instance=workers)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('worker_list')
    else:
        return render(request, 'modify_worker.html', {'form': form})

#LOAN
def loan_list(request):
    query = request.GET.get('q')
    if query:
        loans = Loan.objects.filter(name_icontains=query)
    else:
        loans = Loan.objects.all()
    return render(request, 'loan_list.html', {'loans': loans, 'query': query})

def add_loan(request):
    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_list')
    else:
        form = LoanForm()
    return render(request, 'add_loan.html', {'form': form})

def delete_loan(request, id):
    loans = get_object_or_404(Loan, idLoan=id)
    
    if request.method == 'POST':
        loans.delete()
        return redirect('loan_list')
    else:
        return render(request, 'delete_loan.html', {'loans': loans})
    
def modify_loan(request, id):
    loans = get_object_or_404(Loan, idLoan=id)
    form = LoanForm(instance=loans)

    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loans)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('loan_list')
    else:
        return render(request, 'modify_loan.html', {'form': form})
    
#PPELOAN
def ppe_loan_list(request):
    query = request.GET.get('q')
    if query:
        ppe_loans = PpeLoan.objects.filter(worker__name_icontains=query)
    else:
        ppe_loans = PpeLoan.objects.all()
    print(f"Número de préstamos: {ppe_loans.count()}")
    print(f"Préstamos: {list(ppe_loans)}")
    return render(request, 'ppe_loan_list.html', {'ppe_loans': ppe_loans, 'query': query})

def add_ppe_loan(request):
    if request.method == 'POST':
        form = PpeLoanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ppe_loan_list')
    else:
        form = PpeLoanForm()
    return render(request, 'add_ppe_loan.html', {'form': form})

def delete_ppe_loan(request, id):
    ppe_loans = get_object_or_404(PpeLoan, idPpeLoan=id)
    
    if request.method == 'POST':
        ppe_loans.delete()
        return redirect('ppe_loan_list')
    else:
        return render(request, 'delete_ppe_loan.html', {'ppe_loans': ppe_loans})
    
def modify_ppe_loan(request, id):
    ppe_loans = get_object_or_404(PpeLoan, idPpeLoan=id)
    form = PpeLoanForm(instance=ppe_loans)

    if request.method == 'POST':
        form = LoanForm(request.POST, instance=ppe_loans)
        if form.is_valid():
            form.instance.status = True
            form.save()
            return redirect('ppe_loan_list')
    else:
        return render(request, 'modify_ppe_loan.html', {'form': form})
    
#REGISTER
def register_admin(request):
    if request.method == 'POST':
        form = AdminSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AdminSignUpForm()
    return render(request, 'register_admin.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def exit(request):
    logout(request)
    return redirect('home')