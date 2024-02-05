from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string


# Create your views here.


def index(request):
    data = render_to_string("recon_active/ra.html")
    return HttpResponse(data)


# lunile = {
#     "Jan": "This is the 1st month",
#     "Feb": "This is the 2ed month",
#     "March": "This is the 3rd month"
# }

# def index(request):
#     return HttpResponse("Merge recon_active!")
    
# def dynamic_fct_by_month(request, month):
#     try:
#         luna = lunile[month]
#         return HttpResponse(luna)
#     except:
#         return HttpResponseNotFound("There is no months")
        
    
# def dynamic_fct_by_nr (request, var2):
#     return HttpResponse(var2)

# def dynamic_fct (request,var1):
#     luna = None
#     if var1 == 'january':
#         luna = "There is January"
#     elif var1 == 'february':
#         luna = "There is February"
#     else:
#         return HttpResponseNotFound("No Months")
#     return HttpResponse(luna)
        