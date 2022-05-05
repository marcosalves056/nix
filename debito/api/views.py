from conta_virtual.models import ContaVirtual
from debito.models import Debito
from debito.api.serializers import DebitoSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DebitoViewSet(viewsets.ModelViewSet):

    queryset = Debito.objects.filter(cod_conta = 1)
    serializer_class = DebitoSerializer

    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['valor_inicial'] = 0
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        cod_conta = int((serializer.data['cod_conta']).split('/')[4])
        conta = ContaVirtual.objects.filter(cod_conta = cod_conta)
        saldo_debito = conta.first().saldo_debito
        saldo_atualizado = conta.first().saldo_debito - serializer.data['valor']
        conta.update(saldo_debito = saldo_atualizado)

        id_debito = Debito.objects.all().order_by('-id_debito').first().id_debito
        debito = Debito.objects.filter(id_debito = id_debito)
        debito.update(valor_inicial = saldo_debito)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)        
        