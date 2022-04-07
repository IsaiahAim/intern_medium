from django.db import models


# Create your models here.
class Categorie(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255, blank=True)
    details = models.TextField(max_length=500, blank=True)
    scheduledFor = models.DateTimeField()

    def __str__(self):
        return self.title
