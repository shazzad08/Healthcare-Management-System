from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationApiview

from . import views

router = DefaultRouter()   #router 
router.register("list", views.PatientViewset)   # amader view te 1 ta viewset eijnno 1 ta antena niyeci...
urlpatterns = [
    path("", include(router.urls)),
    path("register/",RegistrationApiview.as_view(),name='register'),
    path('active/<uid64>/<token>/', views.activate, name = 'activate'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),

]