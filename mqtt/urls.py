from django.urls import path
from .views import *


urlpatterns = [
    path('', checkMQTTApi.as_view())
]