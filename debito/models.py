from datetime import datetime
from django.db import models
from conta_virtual.models import ContaVirtual

class Debito(models.Model):
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=110)
    valor = models.FloatField()
    data_trasacao = models.DateTimeField(default=datetime.now)

class HistoricoDebito(models.Model):
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE)
    id_debito = models.ForeignKey(Debito, on_delete=models.CASCADE)
    valor_inicial = models.FloatField()
