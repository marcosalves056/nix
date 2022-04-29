from django.contrib.auth.models import User
from debito.models import Debito
from rest_framework import serializers

class DebitoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debito
        fields = ['cod_conta', 'descricao', 'valor']
        
class DebitoExtratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Debito
        fields = ['descricao', 'valor']