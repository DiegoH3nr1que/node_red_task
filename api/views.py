from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Dados
from .serializers import DadosSerializer, DadosCreateSerializer

class DadosViewSet(viewsets.ViewSet):
    def list(self, request):
        dados = Dados.objects.all()
        serializer = DadosSerializer(dados, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DadosCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Verifica se Botao ou Sensor são True e ResetContador é False
            if serializer.validated_data['Botao'] or serializer.validated_data['Sensor']:
                serializer.validated_data['ValorContagem'] += 1
            if serializer.validated_data['ResetContador']:
                serializer.validated_data['ValorContagem'] = 0
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        dado = Dados.objects.get(pk=pk)
        serializer = DadosSerializer(dado)
        return Response(serializer.data)

    def update(self, request, pk=None):
        dado = Dados.objects.get(pk=pk)
        serializer = DadosCreateSerializer(dado, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        dado = Dados.objects.get(pk=pk)
        dado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
