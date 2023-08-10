from django.shortcuts import render
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer



# Create your views here.

def index(request):
	return render(request, "5breach.html")


class CourseView(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer
