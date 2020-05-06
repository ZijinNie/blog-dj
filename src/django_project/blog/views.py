from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
# 	return HttpResponse('<h1> Blog Home</h1>')

def home(request):
	posts = [
	    {
	        'author': 'CoreyMS',
	        'title': 'Blog Post 1',
	        'content': 'First post content',
	        'date_posted': 'August 27, 2018'
	    },
	    {
	        'author': 'Jane Doe',
	        'title': 'Blog Post 2',
	        'content': 'Second post content',
	        'date_posted': 'August 28, 2018'
	    }
	]
	context = {
		'posts': posts
	}
	return render(request, 'blog/blog_home.html', context)