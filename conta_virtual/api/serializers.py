from django.contrib.auth.models import User
from conta_virtual.models import ContaVirtual
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email']


class ContaVirtualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContaVirtual
        fields = '__all__'
