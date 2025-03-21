from django.urls import path
from .views import login_view, profile_view, register_view, log_out_view

urlpatterns = [
    path('login/',login_view, name='login'),
    path('register/',register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('logout/', log_out_view, name='logout') 
]
