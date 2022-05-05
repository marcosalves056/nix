from django.contrib.auth.models import User
from conta_virtual.models import ContaVirtual
from rest_framework import viewsets, generics
from credito.api.serializers import CreditoSerializer

from credito.models import Credito
from debito.api.serializers import DebitoSerializer
from debito.models import Debito
from .serializers import ContaVirtualSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ContaVirtualViewSet(viewsets.ModelViewSet):

    queryset = ContaVirtual.objects.all().order_by('-cod_conta')
    serializer_class = ContaVirtualSerializer

class ExtratoCredito(generics.ListAPIView):

    def get_queryset(self):
        return Credito.objects.filter(cod_conta = self.kwargs['pk'])

    serializer_class = CreditoSerializer

class ExtratoDebito(generics.ListAPIView):

    def get_queryset(self):
        return Debito.objects.filter(cod_conta = self.kwargs['pk'])
    
    serializer_class = DebitoSerializer