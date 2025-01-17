from cafezinho.models import Contribuicao, Contribuinte
from rest_framework import viewsets, generics
from cafezinho.serializers import ContribuicaoSerializer, ContribuinteSerializer

class ContribuinteViewSet(viewsets.ModelViewSet):
    queryset = Contribuinte.objects.all()
    serializer_class = ContribuinteSerializer

class ContribuicaoViewSet(viewsets.ModelViewSet):
    queryset = Contribuicao.objects.all()
    serializer_class = ContribuicaoSerializer