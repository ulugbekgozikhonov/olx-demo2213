from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Category, Reklama, ReklamaImages
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.decorators import login_required

# @login_required faqat funktsiya yani function base view uchun ishlatilandi
class HomeView(ListView):
    template_name = "index.html"
    model = Category
    context_object_name = "categories"

class AdsView(LoginRequiredMixin, View):    
    login_url = "/users/login/"  # 🔹 Login sahifasi
    redirect_field_name = "next"  # 🔹 Foydalanuvchi login bo‘lgandan keyin yo‘naltirish

    def get(self, request):
        categories = Category.objects.all()
        return render(request, "announce.html", {'categories': categories})
    
    def post(self, request):
        data = request.POST
        photo = request.FILES.get('photo')
        category = Category.objects.filter(name=data.get('category')).first()
        reklama = Reklama.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            category=category,
            phone=data.get('phone'),
            address=data.get('address'),
            user=request.user,
        )
        
        ReklamaImages.objects.create(
            reklama=reklama,
            image=photo,
        )
        
        return redirect('home')

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
