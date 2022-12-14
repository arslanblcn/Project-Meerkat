from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import subDomainSerializer
from .models import Scans
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# Create your views here.
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
class waybackURL(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
class wafDetect(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        
        return Response("Detect Firewall", status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
      import subprocess
      data = {
            'url': request.data.get('url'),
        }
      return Response(subprocess.check_output(["wafw00f", data['url']]), status=status.HTTP_200_OK)  
class dirDiscovery(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        import concurrent.futures 
        import requests, os 
        from pathlib import Path
        context = {}
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
             # Perform the attack using multithreading 
            with concurrent.futures.ThreadPoolExecutor() as executor: 
                for directory in words: 
                    url = BASE_URL + directory 
                    future = executor.submit(requests.get, url)
                    response = future.result() 
                    if response.status_code == 200: 
                        dirs.append(directory)
            return Response(dirs, status=status.HTTP_200_OK)
        else:
            return Response("There is no such a file", status=status.HTTP_200_OK)
        

class subDomainFind(APIView):
    permission_classes = [permissions.IsAuthenticated]
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
            'user': request.user.id
        }
        
        serializer = subDomainSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            res = DNSDumpsterAPI().search(data['domains'])
            subs = []
            dns = res.get("dns_records")
            for host in dns['host']:
                try:
                    response = httpx.get("http://" + str(host['domain']))
                    if response.status_code is 200 or 301 or 302:
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
            #serializer.save()
            return Response(subs, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
