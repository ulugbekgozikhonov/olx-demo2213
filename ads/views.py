from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Reklama, ReklamaImages


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

class AdsDetailView(DetailView):
    template_name = 'single.html'
    model = Reklama
    context_object_name = 'reklama'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["reklama_img"] = ReklamaImages.objects.filter(reklama=self.object).all()
        return context
    
class AdsMainView(ListView):
    template_name = 'main.html'
    model = Reklama
    context_object_name="ads"
    
    def get_queryset(self):
        return Reklama.objects.filter(category__id=self.kwargs["id"]).all()
    

class SearchView(ListView):
    template_name = 'main.html'
    model = Reklama
    context_object_name="ads"
    
    def get_queryset(self):
        search = self.request.GET.get('q')
        if search:
            return Reklama.objects.filter(title__icontains=search).all()
