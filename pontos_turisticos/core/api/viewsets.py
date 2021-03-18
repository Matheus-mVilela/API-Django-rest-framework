from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        queryset = PontoTuristico.objects.all()

        if id:
            queryset = PontoTuristico.objects.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

    # def queryset(self):
    #     return PontoTuristico.objects.all()

    # def list(self, request, *args, **kwargs):
    #     return Response({'teste': 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'helo': request.data['nome']})

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['post', 'get'], detail=True)
    # def denunciar(self, request, pk=None):
    #     pass
