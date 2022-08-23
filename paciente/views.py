from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Paciente
from .forms import pacienteForm
# Create your views here.

def listpacientes(request):
  paciente_list = Paciente.objects.all()
  paginator = Paginator(paciente_list,1)
  page = request.GET.get('page')
  paciente = paginator.get_page(page)

  return render(request, 'paciente/listpacientes.html',{'paciente': paciente})

def pacienteview(request, id):
  paciente  = get_object_or_404(Paciente, pk=id)
  return render(request, 'paciente/pacienteview.html',{'paciente': paciente})

def newpaciente(request):
  if request.method == 'POST':
    form = pacienteForm(request.POST)
    if form.is_valid():
      paciente = form.save(commit=False)
      paciente.ativo='ativo'#salvamos automaticamente como ativo
      paciente.save()
      return redirect('/')
  else:
    form = pacienteForm()
    return render(request, 'paciente/newpaciente.html',{'form': form})  

def editpaciente(request,id):
  paciente  = get_object_or_404(Paciente, pk=id)#recebe dados do banco
  form = pacienteForm(instance=paciente)#recebe dados da variável e insere no form
  if request.method == 'POST':
    form = pacienteForm(request.POST, instance=paciente)#instance é a variável que recebeu os dados do banco
    if form.is_valid():
      paciente.save()
      return redirect('/')
    else:
        return render(request, 'paciente/editpaciente.html',{'form': form, 'paciente': paciente})
  else:
    return render(request, 'paciente/editpaciente.html',{'form': form, 'paciente': paciente})
  
def delpaciente(request,id):
  paciente  = get_object_or_404(Paciente, pk=id)#recebe dados do banco
  paciente.delete()
  messages.info(request, 'Paciente deletado com sucesso!')
  return redirect('/')
  