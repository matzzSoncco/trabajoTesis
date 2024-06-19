from django.urls import path
from .views import home, PersonalProtectionEquipment, add_ppe, register_admin, login, exit
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('ppe/', PersonalProtectionEquipment, name='ppe'),
    path('add/', add_ppe, name='add_ppe'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('material/', views.material_list, name='material_list'),
    path('material/add/', views.add_material, name='add_material'),
    #------------------------------------------------------------URLS--------
    path('materials/edit/<int:pk>/', views.edit_material, name='edit_material'),
    path('materials/delete/<int:pk>/', views.delete_material, name='delete_material'),
    #----------------------------------------------------------------------------------
    path('tool/', views.tool_list, name='tool_list'),
    path('tool/add/', views.add_tool, name='add_tool'),
    path('worker/', views.worker_list, name='worker_list'),
    path('worker/add/', views.add_worker, name='add_worker'),
    path('register_admin/', register_admin, name='register_admin'),
    path('login/', login, name='login'),
    path('logout/', exit, name='exit'),
   
]