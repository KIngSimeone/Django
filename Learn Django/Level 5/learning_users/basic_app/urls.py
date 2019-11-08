from django.urls import path
from basic_app import views

#TEMPLATE URLS
app_name ='basic_app'

urlpatters =[
    path('register/',views.register,name='register')
]