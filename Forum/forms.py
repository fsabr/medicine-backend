from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model  = Post
        fields = {'title', 'description', 'category'}

class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = {'description', 'post_id'}