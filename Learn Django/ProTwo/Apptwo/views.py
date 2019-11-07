from django.shortcuts import render
from django.http import HttpResponse
from Apptwo.forms import NewUserForm


def index(request):
    
    my_dict = {'insert_me':"Hello freaks"}
    return render(request,'Apptwo/index.html',context=my_dict)

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'Apptwo/users.html',{'form':form})
    