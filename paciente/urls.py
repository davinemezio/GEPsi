from django.urls import path
from . import views

urlpatterns = [
    path('', views.menuprincipal),
    path('paciente', views.listpacientes, name='lista-paciente'),
    path('paciente/<int:id>', views.pacienteview, name='view-paciente'),
    path('newpaciente/', views.newpaciente, name='new-paciente'),
    path('editpaciente/<int:id>', views.editpaciente, name='altera-paciente'),
    path('delpaciente/<int:id>', views.delpaciente, name='apaga-paciente'),
    path('consulta', views.marcarconsulta, name='marcar-consulta'),
    path('addconsulta/<int:id>', views.addconsulta, name='add-consulta'),
    path('buscaconsulta', views.buscaconsulta, name='busca-consulta'),
    path('consultaview/<int:id>', views.consultaview, name='view-consulta'),
]
