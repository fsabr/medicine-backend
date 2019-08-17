from django.shortcuts import render, redirect
from Forum.models import Post, Comment
from Forum.forms import PostForm, CommentForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def forum(request):
    if request.method == 'GET':
        return render(request, 'Doctor_website/forum_home.html')
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            print(post)
            post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def forum_category(request, category):
    if request.method == 'GET':
        all_posts = Post.objects.filter(category=category)
        return render(request, 'Doctor_website/forum.html', {"category": category, "posts" : all_posts})
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def new_comment(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        print(form)
        if form.is_valid():
            comment = form.save(commit=True)
            comment.save()
            print(comment.post_id)
            return redirect('post_detail', pk=comment.post_id)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

def post_detail(request, pk):
    #if request.method == 'GET':
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'Doctor_website/forum_post.html', {"post" : post, "comments" : comments})
    # return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)