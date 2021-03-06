from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication


class PontoTuristicoViewSet(ModelViewSet):
    # queryset = PontoTuristico.objects.all()
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAdminUser,)
    serializer_class = PontoTuristicoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nome', 'descricao', 'enderecos__linha1']
    lookup_field = 'nome'  # esse campo de busca tem que ser unico no db

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
