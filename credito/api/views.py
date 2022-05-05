from conta_virtual.models import ContaVirtual
from credito.models import Credito
from credito.api.serializers import CreditoSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import viewsets, generics, status


class CreditoViewSet(viewsets.ModelViewSet):

    queryset = Credito.objects.filter(cod_conta = 1)
    serializer_class = CreditoSerializer
    
    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['valor_inicial'] = 0
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(self.kwargs)

        cod_conta = int((serializer.data['cod_conta']).split('/')[4])
        conta = ContaVirtual.objects.filter(cod_conta = cod_conta)
        saldo_credito = conta.first().saldo_credito
        saldo_atualizado = conta.first().saldo_credito - serializer.data['valor']
        conta.update(saldo_credito = saldo_atualizado)

        print(saldo_credito)
        id_credito = Credito.objects.all().order_by('-id_credito').first().id_credito
        credito = Credito.objects.filter(id_credito = id_credito)
        credito.update(valor_inicial = saldo_credito)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)      