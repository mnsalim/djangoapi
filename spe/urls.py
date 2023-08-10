from django.urls import path, include
from . import views
from rest_framework import routers #allowed us to get and post requests


router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path('', views.index),
    path('', include(router.urls))   
]