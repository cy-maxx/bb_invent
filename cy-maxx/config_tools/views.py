from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from .models import ProjectInfo
from .forms import ProjectInfoForm  

def index(request):
    return render(request, "config_tools/index.html")

def index_amass(request):
    return render(request, 'config_tools/amass.html')

def add_tool_page(request):
    form = ProjectInfoForm()
    if request.method == 'POST':
        form = ProjectInfoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('amass_config')  # Redirect to the index page after saving
    else:
        print("Error Page!")
        # form = ProjectInfoForm()

    return render(request, 'config_tools/add_tool.html', {'form': form})
