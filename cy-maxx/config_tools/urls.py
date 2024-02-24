from django.urls import path
from config_tools import views

urlpatterns = [
    path("", views.index, name="tools_first_page"),
    path('amass',views.index_amass, name='amass_config'),
    path('configsubfinder',views.config_subfinder, name='config_subfinder'),
    path('addtool',views.add_tool_page, name='add_tool_page')
    ]