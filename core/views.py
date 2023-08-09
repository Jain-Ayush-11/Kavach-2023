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
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from selenium.webdriver.chrome.options import Options as ChromeOptions

skip_count = 47

User = get_user_model()

def get_website_report(url=None):

    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.criminalip.io/en/domain/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "query")))
    search = driver.find_element(By.NAME, "query")
    search.send_keys(url)
    search.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'NoResultComponent__PageLink')]")))
    generate_scan = driver.find_element(By.XPATH, "//*[contains(@class, 'NoResultComponent__PageLink')]")
    generate_scan.click()

    time.sleep(5.0)

    driver.exit()
    
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

    def get(self, request, *args, **kwargs):
        try:
            transaction = Transaction.objects.get(transactionHash=self.kwargs['pk'])
            _serializer = TransactionSerializer(instance=transaction)
            return Response(_serializer.data)
        except Transaction.DoesNotExist:
            return Response({'message':'Not Found'}, status=status.HTTP_400_BAD_REQUEST)

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
            return Response({"url": f"https://www.criminalip.io/en/domain/report?scan_id={website_report.report_id}"})
        except WebsiteReport.DoesNotExist:
            report_url = get_website_report(url)
            if report_url is None:
                return Response("url cannot be blank", status=status.HTTP_400_BAD_REQUEST)
            WebsiteReport.objects.create(url=url, report_id=report_url.split("=")[-1])
            return Response({"url": url})

@api_view()
def node_view(request, address):
    # driver.get('https://oxt.me/')
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search-inp')))
    # search_field = driver.find_element(By.ID, 'search-inp')
    # for i in address:
    #     search_field.send_keys(i)
    # search_field.send_keys(Keys.RETURN)

    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'title-icon')))
    # tools_field = driver.find_element(By.CLASS_NAME, 'site-toolbox')
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
    # node_link = tools_field.find_element(By.TAG_NAME, 'a').get_attribute('href')
    # driver.quit()
    # return redirect(node_link)
    return Response({"link": "https://oxt.me/graph/transaction/tiid/2408709084"})

@api_view()
def get_geofencer(request):
    return Response({"url": "https://www.criminalip.io/en/asset/search?query=%22Bitcoin%22+port%3A+8333"})

from rest_framework import views, permissions
from rest_framework.response import Response
from rest_framework import status
from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice

def get_user_totp_device(self, user, confirmed=None):
    devices = devices_for_user(user, confirmed=confirmed)
    for device in devices:
        if isinstance(device, TOTPDevice):
            return device
    
class TOTPCreateView(views.APIView):
    """
    Use this endpoint to set up a new TOTP device
    """
    def get(self, request, format=None):
        user = User.objects.get(username='admin')
        device = get_user_totp_device(self, user)
        if not device:
            device = user.totpdevice_set.create(confirmed=False)
        url = device.config_url
        return Response(url, status=status.HTTP_201_CREATED)
    
class TOTPVerifyView(views.APIView):
    """
    Use this endpoint to verify/enable a TOTP device
    """
    def get(self, request, token, format=None):
        user = User.objects.get(username='admin')
        device = get_user_totp_device(self, user)
        if not device == None and device.verify_token(token):
            if not device.confirmed:
                device.confirmed = True
                device.save()
            return Response(True, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

from django.contrib.auth import authenticate, login

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "success"})
        else:
            return Response({"message": "failed"}, status=status.HTTP_400_BAD_REQUEST)