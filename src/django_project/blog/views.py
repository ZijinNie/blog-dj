from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import (
	LoginRequiredMixin,
	UserPassesTestMixin
	)
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	DeleteView,
	UpdateView
	)
from .models import Post
# Create your views here.

# def home(request):
# 	return HttpResponse('<h1> Blog Home</h1>')

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/blog_home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'blog/blog_home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']

class PostDetailView(DetailView):
	model = Post



class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

	def test_func(self):
		post = self.get_object() 
		if self.request.user == post.author:
			return True
		else:
			return False

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
	model = Post

	success_url = '/'
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

	def test_func(self):
		post = self.get_object() 
		if self.request.user == post.author:
			return True
		else:
			return False