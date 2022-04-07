from rest_framework import viewsets
from .serializers import EventSerializer, CategorySerializer
from .models import Event, Categorie


# Create your views here.
class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorySerializer
