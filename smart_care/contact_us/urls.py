from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()   #router 
router.register("contact_us", views.ContactusViewset)   # amader view te 1 ta viewset eijnno 1 ta antena niyeci...
urlpatterns = [
    path("", include(router.urls)),
]