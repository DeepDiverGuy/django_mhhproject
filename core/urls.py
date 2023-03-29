from django.urls import path
from core import views

urlpatterns = [
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('patient_data/', views.patient_data, name='patient_data'),
    path('pro_data/', views.pro_data, name='pro_data'),    

    path('patient_login/', views.patient_login, name='patient_login'),
    path('patient_logout/', views.patient_logout, name='patient_logout'),
    # path('patientRegister/', views.patientRegister, name='patientRegister'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),

    path('pro_login/', views.pro_login, name='pro_login'),
    path('pro_register/', views.pro_register, name='pro_register'),
    path('pro_dashboard/', views.pro_dashboard, name='pro_dashboard'),
]