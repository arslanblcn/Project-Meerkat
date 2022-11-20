from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import subDomainSerializer
from .models import Scans
from datetime import datetime
# Create your views here.

class dirDiscovery(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self, request):
        import os
        from pathlib import Path
        try:
            # Build paths inside the project like this: BASE_DIR / 'subdir'.
            BASE_DIR = Path(__file__).resolve().parent.parent 
            dir = os.listdir(BASE_DIR / "wordlists/")
            return Response(dir, status=status.HTTP_200_CREATED)
        except:
            return Response("Only json file is exceptable", status=status.HTTP_404_NOT_FOUND)
    def post(self, request, *args, **kwargs):
        import os
        from pathlib import Path
        import json
        data = {
            'filename': request.data.get('filename').replace(" ", ""),
            'content': request.data.get('content')
        }
        if data['filename'].endswith('.json'):
            return Response({'error':'[!] Only json file is exceptable'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                dictionary = {}
                for i in range(len(data['content'])):
                    dictionary[i] = f"{data['content'][i]}"
                # Build paths inside the project like this: BASE_DIR / 'subdir'.
                currentDir = Path(__file__).resolve().parent.parent / 'wordlists'
                with open(os.path.join(currentDir, data['filename']+".json"), "w+") as fp:
                    json.dump(data['content'], fp, indent=4)
                return Response({'success':'[+] Wordlist created!'}, status=status.HTTP_201_CREATED)
            except:
                return Response("[!] There was an error while creating wordlist!", status=status.HTTP_400_BAD_REQUEST)


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
