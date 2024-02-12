from django.urls import path
from recon_active import views

urlpatterns = [
    path("", views.index, name="index_ra")
    ]