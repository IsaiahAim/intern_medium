from rest_framework import serializers
from .models import Event, Categorie


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        models = Event
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Categorie
        fields = "__all__"
