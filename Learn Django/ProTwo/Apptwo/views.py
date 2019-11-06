from django.shortcuts import render
from django.http import HttpResponse
from Apptwo.models import User


def index(request):
    
    my_dict = {'insert_me':"Hello freaks"}
    return render(request,'Apptwo/index.html',context=my_dict)

def users(request):
    users_list = User.objects.order_by('first_name')
    all_users = {'userss':users_list}

    return render (request,'Apptwo/users.html',context=all_users)