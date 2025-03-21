from django.urls import path
from .views import AdsView, HomeView,AdsDetailView,AdsMainView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('announce/',AdsView.as_view(),name="announce"),
    path('single/', AdsDetailView.as_view(),name="single"),
    path('main/', AdsMainView.as_view(),name="main"), 
]
