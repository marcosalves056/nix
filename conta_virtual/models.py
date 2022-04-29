from django.db import models
from django.contrib.auth.models import User

class ContaVirtual(models.Model):
    cod_conta = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=30)
    saldo_debito = models.FloatField()
    saldo_credito = models.FloatField()