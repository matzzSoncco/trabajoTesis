from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from .models.Ppe import Ppe
from .models.Equipment import Equipment
from .models.Worker import Worker
from .models.Material import Material
from .models.Tool import Tool
from .forms import AdminSignUpForm, PpeForm, MaterialForm, WorkerForm, EquipmentForm, ToolForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def PersonalProtectionEquipment(request):
    epp = Ppe.objects.all()
    return render(request, 'ppe.html', {'epp': epp})

def add_ppe(request):
    if request.method == 'POST':
        form = PpeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ppe')
    else:
        form = PpeForm()
    return render(request, 'add_ppe.html', {'form': form})

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'equipment_list.html', {'equipment': equipment})

def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm()
    return render(request, 'add_equipment.html', {'form': form})

#------------------------------------------------------------------------ Añadiendo el CRUD------
def edit_equipment(request, id):
    equipment = get_object_or_404(Equipment, pk=id)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'equipment_list.html', {'form': form, 'edit': True, 'equipment': equipment})

def delete_equipment(request, id):
    equipment = get_object_or_404(Equipment, pk=id)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment_list')
    return render(request, 'equipment_list.html', {'equipment': equipment})

#----------------------------------------------------------------------------Aun no funca



def material_list(request):
    materials = Material.objects.all()
    return render(request, 'material_list.html', {'materials': materials})

def add_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm()
    return render(request, 'add_material.html', {'form': form})
#----------------------------------------------------------------Añadiendo CRUD-------
def edit_material(request, id):
    material = get_object_or_404(Material, pk=id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('material_list')
    else:
        form = MaterialForm(instance=material)
    return render(request, 'material_list.html', {'form': form, 'edit': True, 'material': material})

def delete_material(request, id):
    material = get_object_or_404(Material, pk=id)
    if request.method == 'POST':
        material.delete()
        return redirect('material_list')
    return render(request, 'material_list.html', {'material': material})
#----------------------------------------------------------------------------------

def tool_list(request):
    tools = Tool.objects.all()
    return render(request, 'tool_list.html', {'tools': tools})

def add_tool(request):
    if request.method == 'POST':
        form = ToolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tool_list')
    else:
        form = ToolForm()
    return render(request, 'add_tool.html', {'form': form})



def worker_list(request):
    workers = Worker.objects.all()
    return render(request, 'worker_list.html', {'item': workers})

def add_worker(request):
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)#se agrego files
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm()
    return render(request, 'add_worker.html', {'form': form})
#-----------------------------------------------------------------------------
def edit_worker(request, id):
    worker = get_object_or_404(Worker, pk=id)
    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES, instance=worker)
        if form.is_valid():
            form.save()
            return redirect('worker_list')
    else:
        form = WorkerForm(instance=worker)
    return render(request, 'worker_list.html', {'form': form, 'edit': True, 'worker': worker})

def delete_worker(request, id):
    worker = get_object_or_404(Worker, pk=id)
    if request.method == 'POST':
        worker.delete()
        return redirect('worker_list')
    return render(request, 'worker_list.html', {'worker': worker})
#-----------------------------------------------------------------------------

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