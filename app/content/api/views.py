from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, AllowAny
from content.models import AwardRecognition, HomePageSlider
from content.api.serializers import HomePageSliderSerializer, AwardRecognitionSerializer


# Create your views here.
class HomePageSliderList(viewsets.ModelViewSet):
    queryset = HomePageSlider.objects.filter(display=True)
    serializer_class = HomePageSliderSerializer
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class AwardRecognitionList(viewsets.ModelViewSet):
    queryset = AwardRecognition.objects.all()
    serializer_class = AwardRecognitionSerializer
