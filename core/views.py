from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import redirect
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions

options = ChromeOptions()
options.add_argument("--headless=new")
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

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

@api_view()
def node_view(request, address):
    driver.get('https://oxt.me/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search-inp')))
    search_field = driver.find_element(By.ID, 'search-inp')
    for i in address:
        search_field.send_keys(i)
    search_field.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title-icon')))
    tools_field = driver.find_element(By.CLASS_NAME, 'site-toolbox')
    node_link = tools_field.find_element(By.TAG_NAME, 'a').get_attribute('href')
    driver.quit()
    return redirect(node_link)
