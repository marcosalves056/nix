from django.contrib.auth.models import User
from conta_virtual.models import ContaVirtual
from rest_framework import serializers
from credito.models import Credito
from debito.models import Debito

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']


class ContaVirtualSerializer(serializers.HyperlinkedModelSerializer):
    extrato_debito = serializers.SerializerMethodField()
    extrato_credito = serializers.SerializerMethodField()
    class Meta:
        model = ContaVirtual
        fields = ['id_user','cod_conta','nome_completo','saldo_debito','saldo_credito','extrato_debito','extrato_credito']
    
    def get_extrato_debito(self, obj):
        return Debito.objects.filter(cod_conta = obj.cod_conta).values()
    
    def get_extrato_credito(self, obj):
        return Credito.objects.filter(cod_conta = obj.cod_conta).values()

