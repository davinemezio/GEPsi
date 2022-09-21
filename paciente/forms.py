from dataclasses import fields
from django import forms
from .models import Consulta, Paciente

class pacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    fields = ('nome', 'data_nascimento', 'cpf', 'email', 'celular','ativo')

class consultaForm(forms.ModelForm):
  class Meta:
    model = Consulta
    fields = ('data_consulta',)
