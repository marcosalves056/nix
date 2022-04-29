from django.contrib.auth.models import User
from credito.models import Credito
from rest_framework import serializers

class CreditoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credito
        fields = ['cod_conta', 'descricao', 'valor']
        
class CreditoExtratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credito
        fields = ['descricao', 'valor']

