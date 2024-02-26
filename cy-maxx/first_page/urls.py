from django.urls import path
from . import views
from django.urls import path
from .views import AdaugaDomeniuView, ModificaDomeniuView

urlpatterns = [
    path("",views.index,name='index'),
    path("adaugadomeniu/", AdaugaDomeniuView.as_view(), name='adaugadomeniu_url'),
    path("modificadomeniu/", ModificaDomeniuView.as_view(), name='modificadomeniu_url'),
    ]