from rest_framework import serializers
from .models import models  # Замените на вашу модель

class YourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models
        fields = '__all__'  # Можно указать конкретные поля ['title', 'description'] 
        