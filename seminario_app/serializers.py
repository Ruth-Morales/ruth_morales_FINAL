from rest_framework import serializers
from .models import Inscritos, Institucion

class InscritosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Inscritos
        fields = '__all__'

class InstitucionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'