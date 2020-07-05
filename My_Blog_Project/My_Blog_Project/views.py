from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect, render
import requests
import json

def Index(request):
    return HttpResponseRedirect(reverse('App_Blog:blog_list'))

def about(request):
    return render(request, 'about.html', context={})

def covid_live(request):
    covid_status = False
    if request.method == 'POST':
        country_name = request.POST.get('country_name')
        country = country_name.upper()
        url = 'https://coronavirus-19-api.herokuapp.com/countries/' + str(country) 
        response = requests.get(url)
        covid_status = response.json()
    #diction = {'user':user}
    return render(request, 'covid_live.html', context={'covid_status':covid_status})