from django.shortcuts import render

from .models import Api

def get_all_api(request, *args, **kwargs):
    all_api = Api.objects.all()
    context = {"api_list": all_api}
    return render(request, "api_list/api_list.html", context)
