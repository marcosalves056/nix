from datetime import datetime
from django.db import models
from conta_virtual.models import ContaVirtual

class Credito(models.Model):
    id_credito = models.AutoField(primary_key=True)
    cod_conta = models.ForeignKey(ContaVirtual, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=110)
    valor_inicial = models.FloatField()
    valor = models.FloatField(default=0,null=True)
    data_transacao = models.CharField(max_length=50, default=datetime.now().strftime("%Y.%m.%d %H:%M:%S"))


