from django.urls import path
from jarvisapp.views import Home

urlpatterns = [
    path('', Home.as_view(), name="home")
]