from app.models import Tabsetor
from app.models import Servativ

from rest_framework import serializers

class TabSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tabsetor
        fields = '__all__'

class ServativSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servativ
        fields = '__all__'

# class TabSetorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tabsetor
#         fields = '__all__'