from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

# def home(request):
# 	return HttpResponse('<h1> Blog Home</h1>')

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog_home.html', context)