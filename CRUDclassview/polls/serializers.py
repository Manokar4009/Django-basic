from rest_framework import serializers
from .models import Currencies#, Standards, Countries, Tag

class CurrenciesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Currencies
    fields = '__all__'