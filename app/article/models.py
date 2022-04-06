import uuid
from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.title
