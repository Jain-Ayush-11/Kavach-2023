from django.urls import path
from .views import *

urlpatterns = [
    path('social-media/', SocialMediaList.as_view()),
]