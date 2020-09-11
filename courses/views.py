from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
	queryset = Course.objects.all()
	serializer_class = CourseSerializer