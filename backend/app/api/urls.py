from django.urls import path, include
from .views import subDomainFind,dirDiscovery, waybackURL, bypass403, jsFinder, secretFinder,webAnalyzer, LoginAPI, RegisterAPI

urlpatterns = [
    path("sublist3r/", subDomainFind.as_view(),  name="sublist3r"),
    path("dirDiscovery/", dirDiscovery.as_view(),  name="dirdiscovery"),
    path("wayback/", waybackURL.as_view(),  name="wayback"),
    path("bypass403/", bypass403.as_view(),  name="bypass403"),
    path("jsfinder/", jsFinder.as_view(),  name="jsfinder"),
    path("secretFinder/", secretFinder.as_view(),  name="secretfinder"),
    path("webAnalyzer/", webAnalyzer.as_view(),  name="webanalyzer"),
    path('login/', LoginAPI.as_view(),  name="login"),
    path('register/', RegisterAPI.as_view(),  name="register"),
]