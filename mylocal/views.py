from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'home.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def about(request):
    return render(request, 'about.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts':posts})