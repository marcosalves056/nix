from django.contrib.auth.models import User
from credito.models import Credito
from credito.api.serializers import CreditoSerializer, CreditoExtratoSerializer
from rest_framework import viewsets, generics
# from .serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

class CreditoViewSet(viewsets.ModelViewSet):

    queryset = Credito.objects.filter(cod_conta = 1)
    serializer_class = CreditoSerializer

class CreditoExtratoViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Credito.objects.filter(cod_conta = self.kwargs['pk'])
        return queryset

    serializer_class = CreditoExtratoSerializer