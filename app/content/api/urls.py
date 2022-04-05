from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our views with it.
router = DefaultRouter()
router.register(r'awards', views.AwardRecognitionList, basename="awards")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
