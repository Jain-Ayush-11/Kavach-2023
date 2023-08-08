from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics

# Create your views here.
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

class SocialMediaList(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class TransactionDetail(generics.RetrieveAPIView):
    serializer_class = TransactionSerializer

    def get_object(self):
        return Transaction.objects.get(address=self.kwargs['pk'])

class WatchlistList(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


