from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
# Create your views here.
class helloView(View):
    def get(self, request):
        return HttpResponse('<h1>Hello i am from class View</h1>')
    
class templateCBV(TemplateView):
    template_name = "pages/results.html"



class tt(TemplateView):
    template_name = "pages/results2.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Daiyan Alam'
        context['roll'] = 52
        return context
