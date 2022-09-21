#from re import search
#from turtle import title
from unicodedata import name
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Paciente, Consulta
from .forms import pacienteForm, consultaForm
# Create your views here.

def menuprincipal(request):
  return render(request,'paciente/menuprincipal.html')
def listpacientes(request):
  search = request.GET.get('search')
  if search:
    paciente = Paciente.objects.filter(nome__icontains=search)
  else:
    paciente_list = Paciente.objects.all().order_by('nome')
    paginator = Paginator(paciente_list, 2)
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
  paciente = get_object_or_404(Paciente, pk=id)#recebe dados do banco
  paciente.delete()
  messages.info(request, 'Paciente deletado com sucesso!')
  return redirect('/')

def marcarconsulta(request):
  search = request.GET.get('search')
  if search:
    paciente = Paciente.objects.filter(nome__icontains=search)
  else:
    paciente = ''
  return render(request, 'paciente/consulta.html',{'paciente': paciente})

def addconsulta(request,id):
  paciente = get_object_or_404(Paciente, pk=id)#recebe dados do banco
  if request.method == 'POST':
    form = consultaForm(request.POST)#instance é a variável que recebeu os dados do banco
    if form.is_valid():
      consulta = form.save(commit=False)
      consulta.paciente = paciente
      consulta.save()
      return redirect('consultaview.html')
    else:
      return render(request, 'paciente/addconsulta.html',{'form': form, 'paciente': paciente, 'consulta': consulta})
  else:
    form = consultaForm()
    return render(request, 'paciente/addconsulta.html',{'form': form, 'paciente': paciente})

def buscaconsulta(request):
  search = request.GET.get('search')
  if search:
    paciente = Paciente.objects.filter(nome__icontains=search)
    #consulta = Consulta.objects.all()
    return render(request, 'paciente/buscaconsulta.html',{'paciente': paciente})
  else:   
    paciente = ''
    #consulta = get_object_or_404(Consulta)#recebe dados do banco
    #return render(request, 'paciente/buscaconsulta.html',{'consulta': consulta})
    return render(request, 'paciente/buscaconsulta.html', {'paciente': paciente})

def consultaview(request, id):
  #consulta  = get_object_or_404(Consulta, pk=id)
  consulta = Consulta.objects.filter(paciente=id)
  paciente = Paciente.objects.filter(pk=id)
  return render(request, 'paciente/consultaview.html', context = {
    'consulta': consulta,
    'paciente': paciente
  })