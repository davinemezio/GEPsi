from dataclasses import fields
from django import forms
from .models import Paciente

class pacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    fields = ('nome', 'data_nascimento', 'cpf', 'email', 'celular','ativo')