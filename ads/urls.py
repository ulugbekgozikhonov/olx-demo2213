from django.urls import path
from .views import AdsView, HomeView,AdsDetailView,AdsMainView, SearchView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('announce/',AdsView.as_view(),name="announce"),
    path('single/<int:pk>', AdsDetailView.as_view(),name="single"),
    path('main/<int:id>', AdsMainView.as_view(),name="main"),
    path('search/', SearchView.as_view(),name="search"),
]
