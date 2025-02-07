from django.shortcuts import render
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
        "categories": categories
    }
    return render (request, 'cook/index.html', context)


def category_list(request, pk):
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        "title": posts[0].category,
        "posts": posts,
        "categories": categories
    }
    return render (request, 'cook/index.html', context)

def post_detail(request, pk):
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(wathed=F('wathed') + 1)
    ext_post = Post.objects.all().order_by('-wathed')[:5]
    context = { 
               'title': article.title,
               'post': article,
               'ext_post': ext_post,
        
    }
    return render(request, 'cook/article_detail.html', context)


def add_post(request):
    if request.method == 'POST':
        pass
    else:
        form = PostAddForm()
        
    context = {
        'form': form,
        'title': 'Добавить статью',
   
    }
    return render(request, 'cook/article_add_form.html', context)
    