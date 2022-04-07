from django.db import models


# Create your models here.
class HomePageSlider(models.Model):
    article = models.ForeignKey("article.Article", on_delete=models.CASCADE, blank=True)
    display = models.BooleanField(default=True)

    def __str__(self):
        return self.article


class AwardRecognition(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='award/')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.title
