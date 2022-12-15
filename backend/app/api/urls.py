from django.urls import path
from .views import subDomainFind,dirDiscovery, waybackURL, wafDetect, bypass403, jsFinder, secretFinder
urlpatterns = [
    path("sublist3r/", subDomainFind.as_view(),  name="sublist3r"),
    path("dirDiscovery/", dirDiscovery.as_view(),  name="dirdiscovery"),
    path("wayback/", waybackURL.as_view(),  name="wayback"),
    path("wafdetect/", wafDetect.as_view(),  name="wafdetect"),
    path("bypass403/", bypass403.as_view(),  name="bypass403"),
    path("jsfinder/", jsFinder.as_view(),  name="jsfinder"),
    path("secretFinder/", secretFinder.as_view(),  name="secretfinder"),
]