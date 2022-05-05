from conta_virtual.models import ContaVirtual
from credito.models import Credito
from rest_framework import serializers

class CreditoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credito
        fields = ['cod_conta', 'descricao', 'valor', 'valor_inicial']
    def validate(self, obj):
        print(obj['cod_conta'])
        conta = ContaVirtual.objects.get(cod_conta = obj['cod_conta'].cod_conta)
        if conta.saldo_credito < obj['valor']:
            raise serializers.ValidationError({'valor' : f'Saldo insuficiente. Seu limite de credito é: R${"{:.2f}".format(conta.saldo_credito)}'})
        return obj
