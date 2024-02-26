from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import get_object_or_404
from .models import Domain

# Create your views here.

def index(request):
    return render(request, "first_page/index.html")
def adauga_domeniu(request):
    return render(request, "first_page/adaugadomeniu.html")
def adauga_subdomeniu(request):
    return render(request, "first_page/adaugasubdomeniu.html")

# your_app_name/views.py

class AdaugaDomeniuView(CreateView):
    model = Domain
    template_name = 'first_page/adaugadomeniu.html'
    fields = ['domain', 'site', 'bugbounty']
    success_url = reverse_lazy('index')  # Update 'home' with the name of your home page

class ModificaDomeniuView(UpdateView):
    model = Domain
    template_name = 'first_page/modificadomeniu.html'
    fields = ['site', 'bugbounty']
    success_url = reverse_lazy('index')  # Update 'home' with the name of your home page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domains'] = Domain.objects.all()
        return context
