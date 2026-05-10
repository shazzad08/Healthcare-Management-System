from django.shortcuts import render
from rest_framework import viewsets, filters
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .pagination import MyPagination
from rest_framework.filters import BaseFilterBackend

# Create your views here.


class DoctorViewset(viewsets.ModelViewSet):

    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    
    #for pagination
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    search_fields = [
        'user__first_name',
        'user__email',
        'designation__name',
        'specialization'
    ]
    
class SpecificDoctorAvailableTime(BaseFilterBackend):    #ekta specific doctor er available time ber korar jnno filter krtesi

    def filter_queryset(self, request, queryset, view):

        doctor_id = request.query_params.get('doctor_id')

        if doctor_id:
            queryset = queryset.filter(id=doctor_id)

        return queryset
    
class SpecializationViewset(viewsets.ModelViewSet):
    
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer
    
    
class DesignationViewset(viewsets.ModelViewSet):

    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    
    filter_backends = [SpecificDoctorAvailableTime]


class ReviewViewset(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]  #IsAuthenticated → শুধু logged-in user

    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    filter_backends = [filters.SearchFilter]
    pagination_class = MyPagination
    
    
