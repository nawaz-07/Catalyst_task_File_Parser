from rest_framework import serializers
from .models import CSVData

class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSVData
        fields = '__all__'