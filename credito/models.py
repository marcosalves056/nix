from datetime import datetime
from django.db import models
from conta_virtual.models import ContaVirtual

class Credito(models.Model):
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=110)
    valor = models.FloatField()
    data_transacao = models.DateTimeField(default=datetime.now)

class HistoricoCredito(models.Model):
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE)
    id_debito = models.ForeignKey(Credito, on_delete=models.CASCADE)
    valor_inicial = models.FloatField()

