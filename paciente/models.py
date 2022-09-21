from django.db import models
# Create your models here.
class Paciente(models.Model):
  STATUS = (('ativo','Ativo'), ('inativo','Inativo'))

  nome = models.CharField(max_length=100)
  data_nascimento = models.DateField()
  cpf = models.CharField(max_length=11)
  email = models.CharField(max_length=100)
  celular = models.CharField(max_length=12)
  ativo = models.CharField(max_length=7, choices=STATUS)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nome

class Consulta(models.Model):
  data_consulta = models.DateField()
  paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return (self.data_consulta, self.paciente.id)