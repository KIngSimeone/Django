from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dict = {'insert_me':"Hello freaks"}
    return render(request,'Apptwo/index.html',context=my_dict)