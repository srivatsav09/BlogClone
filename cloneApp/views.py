from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView,)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from cloneApp.forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from cloneApp.models import Post,Comment
from django.utils import timezone

class AboutView(TemplateView):
    template_name='about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')
#sql query on model lte - less than or equal to (grab published dates that are less than or equal 
#to the current time and then order them by published date either ascending or descending)

class PostDetailView(DetailView):
    model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/' #if person is not logged in where should they go
    redirect_field_name = 'cloneApp/post_detail.html' #redirect them to detail view
    form_class = PostForm

    model = Post


class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url = '/login/' #if person is not logged in where should they go
    redirect_field_name = 'cloneApp/post_detail.html' #redirect them to detail view
    form_class = PostForm

    model = Post

class postDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class draftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'cloneApp/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(pub_date__isnull=True).order_by('create_date')


# Create your views here.

@login_required
def add_comments_to_post(request,pk):
    post = get_object_or_404(Post,pk = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'cloneApp/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)