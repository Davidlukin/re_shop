from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h4>Главная</h4>')

def abaut(request):
    return HttpResponse('<h5>Страница про нас </5>')