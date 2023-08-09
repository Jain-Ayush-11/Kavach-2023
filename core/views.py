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

from selenium.webdriver.chrome.options import Options as ChromeOptions

skip_count = 47

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

@api_view()
def demixing(request):
    _response = [
        '08f1dcd0371b544dacc3901e42ddc278519f123c87f8b41516238a40ecd499fe',
        '93ed68dd96b24f2127cfa610361fc9c94a48f99b864bd78b3cdce5d1342003b1',
        '370e129b49912101b1e4cfb4644f9f785151c87f50f955fad831e49eeca251e7',
        '9f51a40a223ce57e47faab8f95306a32c015c3e4ac39bc6c50288342384408bb',
        'bf79ecc12697ad5f5e3af7620e79f118e7a4438557e11c13b236463dfc08fe17',
        'c738cbb655ecbea7a95ce97a0d9455880af70e5e3bf9d29f241ee9fb5b30c981',
        'ec985724c7e2f5bba6b93bb01066760a113005790e3ffa37218608d495dc759d'
    ]
    return Response(_response)
import requests

def get_destinations(address_or_tx):

    if is_valid_address(address_or_tx) or is_valid_tx_hash(address_or_tx):
        url = f"https://api.blockcypher.com/v1/btc/main/{'addrs' if is_valid_address(address_or_tx) else 'txs'}/{address_or_tx}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            destinations = []
            if is_valid_address(address_or_tx):
                for tx in data["txs"]:
                    for output in tx["outputs"]:
                        if "spent_by" not in output:
                            destination = output["addresses"]
                            if destination is not None:
                                destination = destination[0]
                                if destination not in destinations:
                                    destinations.append(destination)
            else:
                for output in data["outputs"]:

                    destination = output["addresses"]
                    # Check if the destination address is not None
                    if destination is not None:
                        # Get the first element of the destination address list
                        destination = destination[0]
                        # Append it to the destinations list if not already present
                        if destination not in destinations:
                            destinations.append(destination)
            # Return the destinations list
            return destinations
        else:
            # Return an empty list if the response is invalid
            return []
    else:
        # Return an empty list if the input is invalid
        return []

# Define a helper function to check if a string is a valid bitcoin address
def is_valid_address(address):
    # Check if the address length is between 26 and 35 characters
    if len(address) < 26 or len(address) > 35:
        return False
    # Check if the address starts with 1, 3, or bc1 (for legacy, segwit, and bech32 formats respectively)
    if not (address.startswith("1") or address.startswith("3") or address.startswith("bc1")):
        return False
    # Check if the address contains only alphanumeric characters (excluding uppercase O, uppercase I, lowercase l, and number 0)
    valid_chars = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    for char in address:
        if char not in valid_chars:
            return False
    # TODO: Add more validation rules such as checksum and version byte checks (optional)
    return True

# Define a helper function to check if a string is a valid transaction hash
def is_valid_tx_hash(tx_hash):
    # Check if the transaction hash length is 64 characters (32 bytes)
    if len(tx_hash) != 64:
        return False
    # Check if the transaction hash contains only hexadecimal characters (0-9 and a-f)
    hex_chars = "0123456789abcdef"
    for char in tx_hash:
        if char not in hex_chars:
            return False
    return True

@api_view()
def get_dest(request, tx_id):
    arr = get_destinations(tx_id)
    return Response(arr)

class ReportView(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

