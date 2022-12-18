from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, generics
from rest_framework import status
from .serializers import subDomainSerializer, UserSerializer, RegisterSerializer
from knox.models import AuthToken
from .models import Scans
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Create your views here.
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class bypass403(APIView):
    def post(self, request, *args, **kwargs):
        import requests
        data = {
            'url': request.data.get('url'),
            'path': request.data.get('path')
        }
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        BASE_URL = data['url'] + data['path']
        response = requests.get(BASE_URL, headers=headers, verify=False)
        findings = []
        if response.status_code == 403:
            payloads = ["X-Originating-IP",
                        "X-Forwarded-For",
                        "X-Forwarded",
                        "Forwarded-For",
                        "X-Remote-IP",
                        "X-Remote-Addr",
                        "X-ProxyUser-Ip",
                        "X-Original-URL",
                        "Client-IP",
                        "True-Client-IP",
                        "Cluster-Client-IP",
                        "X-ProxyUser-Ip",
                        "Host"]
            for header in payloads:
                headers[header] = "127.0.0.1"
                resp = requests.get(BASE_URL, headers=headers,verify=False)
                if resp.status_code <= 400:
                    findings.append(resp)
        return Response(findings, status=status.HTTP_200_OK)

class webAnalyzer(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        from Wappalyzer import Wappalyzer, WebPage
        data = {
            'urls': request.data.get('urls')
        }
        results = {}
        for url in data['urls']:
            webpage = WebPage.new_from_url('http://' + str(url))
            wappalyzer = Wappalyzer.latest()
            response = wappalyzer.analyze(webpage)
            results[url] = response
        return Response(results, status=status.HTTP_200_OK)
class secretFinder(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def post (self, request, *args, **kwargs):
        import re
        from bs4 import BeautifulSoup
        import requests

        data = {
            'urls': request.data.get('urls')
        }
        api_key_regex = r"([0-9a-zA-Z/+]{40})"

        finding = {"url":[], 'key': []}
        str1 = ""
        # Loop over the URLs
        for url in data['urls']:
            # Make a GET request to the URL
            response = requests.get(url)
            # Parse the response as HTML
            soup = BeautifulSoup(response.text, "html.parser")
            # Use the regular expression to find the API key in the HTML
            api_key = re.findall(api_key_regex, str(soup))
            
            # If an API key was found, print it
            if api_key is not None:
                finding["url"].append(url)
                finding['key'].append(str1.join(api_key))
        return Response(finding, status=status.HTTP_200_OK)
                    
class jsFinder(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        from bs4 import BeautifulSoup
        import requests
        data = {'url': request.data.get('url')}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        response = requests.get("http://" + str(data['url']), verify=False, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Iterate over the script tags and collect the URLs of the JavaScript files
        js_files = []
        for script in soup.find_all("script"):
            if script.attrs.get("src"):
                url = script.attrs.get("src")
                js_files.append(url)
        return Response(js_files, status=status.HTTP_200_OK)

class waybackURL(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        
        return Response("Search historic URLs", status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        import waybackpy
        data = {
            'url': request.data.get('url'),
            'year': request.data.get('year')
        }
        UA = "Mozilla/5.0 (iPad; CPU OS 8_1_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B435 Safari/600.1.4"
        knowns = waybackpy.Url(url=data['url'], user_agent=UA).near(year=data['year']).known_urls(subdomain=False) # alive and subdomain are optional.
        return Response(knowns, status=status.HTTP_200_OK)
class dirDiscovery(APIView):
    #permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        import os
        from pathlib import Path
        BASE_DIR = Path(__file__).resolve().parent.parent 
        wordlist = os.listdir(str(BASE_DIR) + "/wordlists/")
        return Response(wordlist, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        import requests, os
        import concurrent.futures
        from pathlib import Path
        data = {
            'url': request.data.get('url'),
            'filename': request.data.get('filename')
        }
        BASE_DIR = Path(__file__).resolve().parent.parent
        BASE_URL = data['url'] # A list of potential directory names to try 
        wordlist = str(BASE_DIR) + f"/wordlists/{data['filename']}"
        dirs = []
        
        if os.path.exists(wordlist):
            with open(wordlist, 'r') as fp:
                words = fp.readlines()
            for directory in words: 
                dirs.append(str(BASE_URL) + "/" + directory)
            successful_urls = []

            # Create a ThreadPoolExecutor and submit a task for each URL
            with concurrent.futures.ThreadPoolExecutor() as executor:
                tasks = [executor.submit(lambda url: successful_urls.append(url) if requests.get(url, verify=False).status_code == 200 else None, url) for url in dirs]
            # Wait for all tasks to finish
            concurrent.futures.wait(tasks)
            return Response(successful_urls, status=status.HTTP_200_OK)
        else:
            return Response("There is no such a file", status=status.HTTP_200_OK)
        

class subDomainFind(APIView):
   # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        scans = Scans.objects.filter(user=request.user.id)
        serializer = subDomainSerializer(scans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
        import httpx
        data = {
            'scanname': request.data.get('scanname'),
            'domains' : request.data.get('domains'),
            'created_at': datetime.now(),
            'user': request.data.get('user')
        }
        
        serializer = subDomainSerializer(data=data)
        if serializer.is_valid():
            res = DNSDumpsterAPI().search(data['domains'])
            subs = []
            dns = res.get("dns_records")
            for host in dns['host']:
                try:
                    response = httpx.get("http://" + str(host['domain']))
                    accepted_status = [200, 301, 302]
                    if response.status_code in accepted_status:
                        #print(host['domain'])
                        context = {
                            'domain': host['domain'],
                            'ip': host['ip'],
                            'reverse_dns': host['reverse_dns'],
                            'as': host['as'],
                            'provider': host['provider'],
                            'country': host['country'],
                            'header': host['header']
                        }
                        subs.append(context)
                        print(context)
                except httpx.HTTPError as exc:
                    print(f"HTTP Exception for {exc.request.url} - {exc}")
            #print(res)
            serializer.save()
            return Response(subs, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
