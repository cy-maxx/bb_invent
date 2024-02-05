from django.urls import path
from . import views

urlpatterns = [
    path("",views.index)
    # path("0", views.index),
    # path("<int:var2>", views.dynamic_fct_by_nr),
    # path("<str:var1>", views.dynamic_fct),
    # path("<str:month>", views.dynamic_fct_by_month)
    ]