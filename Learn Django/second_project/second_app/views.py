from django.shortcuts import render


def index(request):
    my_dict = {'insert_content': "Whats good"}
    return render(request, 'second_app/index.html', context= my_dict )
     