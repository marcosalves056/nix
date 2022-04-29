from django.contrib.auth.models import User, Group
from conta_virtual.models import ContaVirtual
from rest_framework import viewsets
from .serializers import ContaVirtualSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class ContaVirtualViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ContaVirtual.objects.all().order_by('-cod_conta')
    serializer_class = ContaVirtualSerializer