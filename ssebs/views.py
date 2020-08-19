from django.shortcuts import render
from ssebs.models import post,notice
from .forms import CommentForm

# Create your views here.

def noticees(request):
    
    noticee = notice.objects.all()
    context = {'noticee': noticee}
    return render(request, "notice.html", context)




def ssebs_index(request):
    posts = post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, "ssebs_index.html", context)

def ssebs_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def ssebs_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
       
    

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return render(request, "ssebs_detail.html", context)