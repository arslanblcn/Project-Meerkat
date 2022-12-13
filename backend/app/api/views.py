from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import subDomainSerializer
from .models import Scans
from datetime import datetime

# Create your views here.

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
        import requests, threading, queue
        data = {
            'url': request.data.get('url'),
            'wordlist': request.data.get('wordlist'),
            'thread_num': request.data.get('thread_num')
        }
        def scanner():
            hits = []
            statusList = [200,301,302,403]
            try:
                while not q.empty():
                    inject = q.get()
                    kn0ck = '{}/{}'.format(data['url'],inject)
                    r = requests.get(kn0ck)
                    ret = f'{r.status_code}'           
                    if ret in statusList:
                        hits.append((kn0ck,ret))
                    return Response({f"{kn0ck} : {ret}"}, status=status.HTTP_200_OK)
            except KeyboardInterrupt:
                print("Program terminated by user.")

        count = 0
        q = queue.Queue()
        for word in data['wordlist']:
            q.put(word)
            count += 1
        # Handling threads
        ts = []
        for i in range(0,data['thread_num']):
            try:
                t = threading.Thread(target=scanner)
                ts.append(t)
                t.start()
            except Exception as e:
                print(e)
        for t in ts:
            t.join()

class subDomainFind(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        scans = Scans.objects.filter(user=request.user.id)
        serializer = subDomainSerializer(scans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, *args, **kwargs):
        from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
        data = {
            'scanname': request.data.get('scanname'),
            'domains' : request.data.get('domains'),
            'created_at': datetime.now(),
            'user': request.user.id
        }
        print(data)
        serializer = subDomainSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            res = DNSDumpsterAPI().search(data['domains'])
            print(res)
            serializer.save()
            return Response(res, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
