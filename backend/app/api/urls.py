from django.urls import path
from .views import subDomainFind
urlpatterns = [
    path("sublist3r/", subDomainFind.as_view(),  name="sublist3r")
]