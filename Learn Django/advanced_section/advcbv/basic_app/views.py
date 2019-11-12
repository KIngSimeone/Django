from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.views.generic import ListView,DetailView
from . import models

# Create your views here.
class SchoolListView(ListView):
    model = models.School

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

        
        
 