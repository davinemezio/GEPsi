from django.urls import path
from . import views

urlpatterns = [
    path('', views.listpacientes, name='lista-paciente'),
    path('paciente/<int:id>', views.pacienteview, name='view-paciente'),
    path('newpaciente/', views.newpaciente, name='new-paciente'),
    path('editpaciente/<int:id>', views.editpaciente, name='altera-paciente'),
    path('delpaciente/<int:id>', views.delpaciente, name='apaga-paciente'),
]
