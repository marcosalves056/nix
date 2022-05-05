from datetime import datetime
from django.db import models
from conta_virtual.models import ContaVirtual

class Debito(models.Model):
    id_debito = models.AutoField(primary_key=True)
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE, default=1)
    descricao = models.CharField(max_length=110)
    valor_inicial = models.FloatField()
    valor = models.FloatField(default=0,null=True)
    data_transacao = models.CharField(max_length=50,default=datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
