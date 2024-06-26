from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, PersonalProtectionEquipment, add_ppe, register_admin, login, exit
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('ppe/', PersonalProtectionEquipment, name='ppe'),
    path('add/', add_ppe, name='add_ppe'),
    path('ppe/modify/<str:id>/', views.modify_ppe, name='modify_ppe'),
    path('ppe/delete/<str:id>/', views.delete_ppe, name='delete_ppe'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('equipment/delete/<str:id>/', views.delete_equipment, name='delete_equipment'),
    path('equipment/modify/<str:id>/', views.modify_equipment, name='modify_equipment'),
    path('equipment/add/', views.add_equipment, name='add_equipment'),
    path('material/', views.material_list, name='material_list'),
    path('material/add/', views.add_material, name='add_material'),
    path('materials/modify/<str:id>/', views.modify_material, name='modify_material'),
    path('materials/delete/<str:id>/', views.delete_material, name='delete_material'),
    path('tool/', views.tool_list, name='tool_list'),
    path('tool/add/', views.add_tool, name='add_tool'),
    path('tool/delete/<str:id>/', views.delete_tool, name='delete_tool'),
    path('tool/modify/<str:id>/', views.modify_tool, name='modify_tool'),
    path('worker/', views.worker_list, name='worker_list'),
    path('worker/add/', views.add_worker, name='add_worker'),
    path('worker/delete/<int:id>/', views.delete_worker, name='delete_worker'),
    path('worker/modify/<int:id>/', views.modify_worker, name='modify_worker'),
    path('loan/', views.loan_list, name='loan_list'),
    path('loan/add/', views.add_loan, name='add_loan'),
    path('loan/delete/<int:id>/', views.delete_loan, name='delete_loan'),
    path('loan/modify/<int:id>/', views.modify_loan, name='modify_loan'),
    path('ppeloan/', views.ppe_loan_list, name='ppe_loan_list'),
    path('ppeloan/add/', views.add_ppe_loan, name='add_ppe_loan'),
    path('ppeloan/delete/<int:id>/', views.delete_ppe_loan, name='delete_ppe_loan'),
    path('ppeloan/modify/<int:id>/', views.modify_ppe_loan, name='modify_ppe_loan'),
    path('register_admin/', register_admin, name='register_admin'),
    path('login/', login, name='login'),
    path('logout/', exit, name='exit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)