from rest_framework import serializers
from .models import Dados

class DadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = '__all__'  # Para exibir todos os campos

class DadosCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dados
        fields = ['Botao', 'Sensor', 'ResetContador', 'ValorContagem']  # Apenas os campos necessários para criar um novo objeto
