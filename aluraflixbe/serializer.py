from rest_framework import serializers
from aluraflixbe.models import Video, Categoria
from aluraflixbe.validators import *

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        ordering = ['id']
    

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        ordering = ['id']

    def validate(self, data):
        if not cor_valida(data['cor']):
            raise serializers.ValidationError({'cor':'A cor deve estar no formato hexadecimal iniciado com #.'})
        return data


class ListaVideosPorCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
        ordering = ['id']