from django.contrib.auth.models import User
from conta_virtual.models import ContaVirtual
from debito.models import Debito
from rest_framework import serializers



class DebitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debito
        fields = ['id_debito', 'cod_conta', 'descricao', 'valor','valor_inicial']
     
    def validate(self, obj):
        print(obj['cod_conta'])
        conta = ContaVirtual.objects.get(cod_conta = obj['cod_conta'].cod_conta)
        if conta.saldo_debito < obj['valor']:
            raise serializers.ValidationError({'valor' : f'Saldo insuficiente. Seu saldo de debito é: R${"{:.2f}".format(conta.saldo_debito)}'})
        return obj