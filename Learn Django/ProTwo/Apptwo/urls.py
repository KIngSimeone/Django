from Apptwo import views
from django.urls import path


urlpatterns = [
    path('',views.index,name='index'),
    path('users/', views.users, name ='users')
]