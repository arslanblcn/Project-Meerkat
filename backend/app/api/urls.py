from django.urls import path
from .views import subDomainFind,dirDiscovery, waybackURL, bypass403, jsFinder, secretFinder,webAnalyzer, RegisterAPI, LoginAPI
from knox import views as knox_views
urlpatterns = [
    path("sublist3r/", subDomainFind.as_view(),  name="sublist3r"),
    path("dirDiscovery/", dirDiscovery.as_view(),  name="dirdiscovery"),
    path("wayback/", waybackURL.as_view(),  name="wayback"),
    path("bypass403/", bypass403.as_view(),  name="bypass403"),
    path("jsfinder/", jsFinder.as_view(),  name="jsfinder"),
    path("secretFinder/", secretFinder.as_view(),  name="secretfinder"),
    path("webAnalyzer/", webAnalyzer.as_view(),  name="webanalyzer"),
    path("register/", RegisterAPI.as_view(),  name="register"),
    path("login/", LoginAPI.as_view(),  name="login"),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]