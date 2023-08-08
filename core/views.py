from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import generics
from django.shortcuts import redirect
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from rest_framework import status

def get_website_report(url=None):
    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.criminalip.io/en/domain/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "query")))
    search = driver.find_element(By.NAME, "query")
    search.send_keys(url)
    search.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'NoResultComponent__PageLink')]")))
    generate_scan = driver.find_element(By.XPATH, "//*[contains(@class, 'NoResultComponent__PageLink')]")
    generate_scan.click()

    time.sleep(3.0)
    
    return driver.current_url
    
    

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

class WebsiteReportView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        url = request.query_params.get('url', None)
        if url is None:
            return Response("url cannot be blank", status=status.HTTP_400_BAD_REQUEST)
        try:
            website_report = WebsiteReport.objects.get(url=url)
            return redirect(f"https://www.criminalip.io/en/domain/report?scan_id={website_report.report_id}")
        except WebsiteReport.DoesNotExist:
            report_url = get_website_report(url)
            if report_url is None:
                return Response("url cannot be blank", status=status.HTTP_400_BAD_REQUEST)
            WebsiteReport.objects.create(url=url, report_id=report_url.split("=")[-1])
            return Response({"url": url})