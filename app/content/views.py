from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import AwardRecognition, HomePageSlider
from .serializers import HomePageSliderSerializer, AwardRecognitionSerializer


# Create your views here.
class HomePageSliderViewsets(viewsets.ModelViewSet):
    queryset = HomePageSlider.objects.filter(display=True)
    serializer_class = HomePageSliderSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class AwardRecognitionViewsets(viewsets.ModelViewSet):
    queryset = AwardRecognition.objects.all()
    serializer_class = AwardRecognitionSerializer
