from rest_framework import serializers
from .models import Tutorial

class TutorialSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tutorial
        fields = ('id',
                    'titulo',
                    'descripcion',
                    'publicado')

        