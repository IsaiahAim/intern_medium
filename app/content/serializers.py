from .models import HomePageSlider, AwardRecognition
from rest_framework.serializers import ModelSerializer, ValidationError


class AwardRecognitionSerializer(ModelSerializer):
    
    class Meta:
        model = AwardRecognition
        fields = "__all__"


class HomePageSliderSerializer(ModelSerializer):
    
    class Meta:
        model = HomePageSlider
        fields = "__all__"
        
    def validate(self, attrs):
        article = attrs['article']
        article_filter = HomePageSlider.objects.filter(article=article)
        if article_filter.exists():
            raise ValidationError('Article already exists')
        return super().validate(attrs)
