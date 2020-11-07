from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import post, message
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.

def contact(request):
    if request.method=="POST":
        
        names = request.POST["names"]
        messager = request.POST["messager"]
        numbers = request.POST["numbers"]
        forms= message(name=names, messagei = messager, number = numbers )
        forms.save()
        messages.success(request, "submited!")

        
    return render(request, 'contact.html')
  

class HomeView(ListView):
    model = post
    template_name = 'index.html'
    ordering = ['-Date']

class detailView(DetailView):
    model = post
    template_name ='detail.html'

class create(CreateView):
    model = post
    template_name = 'create.html'
    fields = '__all__'
class edit(UpdateView):
    model = post
    template_name = 'edit.html'
    fields = '__all__'

class delete(DeleteView):
    model = post
    template_name = 'delete.html'
    success_url = reverse_lazy('index')

