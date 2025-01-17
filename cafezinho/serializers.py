from rest_framework import serializers
from cafezinho.models import Contribuicao, Contribuinte

class ContribuinteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribuinte
        fields = '__all__'

class ContribuicaoSerializer(serializers.ModelSerializer):
    contribuinte = serializers.PrimaryKeyRelatedField(queryset=Contribuinte.objects.all(), write_only=True)
    contribuinte_nome = serializers.CharField(source='contribuinte.nome', read_only=True)
    class Meta:
        model = Contribuicao
        fields = ['id', 'descricao_da_contribuicao', 'data', 'contribuinte', 'contribuinte_nome']

