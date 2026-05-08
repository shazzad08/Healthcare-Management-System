from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
# for sending email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.shortcuts import redirect
# Create your views here.

class PatientViewset(viewsets.ModelViewSet):

    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class RegistrationApiview(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self,request):
        serializer= self.serializer_class(data= request.data)
        
        
        if serializer.is_valid():
            user = serializer.save()
            #print(user)


            #-----Email Feature Adding-----#


            token = default_token_generator.make_token(user)    #Creates unique secure token + This token is used to verify the user securely.
            #print("token ", token)
            uid = urlsafe_base64_encode(force_bytes(user.pk))  #Converts user id into encoded format + This hides raw database ID.
            #print("uid ", uid)
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"
            email_subject = "Confirm Your Email"
            email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})

            email = EmailMultiAlternatives(email_subject , '', to=[user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response("Check your mail for confirmation")
        return Response(serializer.errors)