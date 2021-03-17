from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacoesSerializer


class AvaliacoesViewSet(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

