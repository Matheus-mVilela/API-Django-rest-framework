from rest_framework.serializers import ModelSerializer
from avaliacoes.models import Avaliacoes


class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('user', 'comentario', 'nota', 'data')

