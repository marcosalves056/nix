from django.contrib.auth.models import User, Group
from debito.models import Debito
from debito.api.serializers import DebitoSerializer, DebitoExtratoSerializer
from rest_framework import viewsets, generics
# from .serializers import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


class DebitoViewSet(viewsets.ModelViewSet):

    queryset = Debito.objects.filter(cod_conta = 1)
    serializer_class = DebitoSerializer

class DebitoExtratoViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Debito.objects.filter(cod_conta = self.kwargs['pk'])
        return queryset

    serializer_class = DebitoExtratoSerializer