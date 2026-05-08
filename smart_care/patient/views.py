from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class PatientViewset(viewsets.ModelViewSet):

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class RegistrationApiview(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self,request):
        serializer= self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registration Successful"})
        return Response(serializer.errors)