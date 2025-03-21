from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Category


# def home_view(request):
#     context = {
#         "categories":  Category.objects.all()
#     }
    
#     return render(request,'index.html', context)

class HomeView(ListView):
    template_name = "index.html"
    model = Category
    context_object_name = "categories"

class AdsView(TemplateView):
    template_name = 'announce.html'

class AdsDetailView(TemplateView):
    template_name = 'single.html'
    
class AdsMainView(TemplateView):
    template_name = 'main.html'