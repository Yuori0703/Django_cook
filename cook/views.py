from django.shortcuts import render, redirect
from .models import Category, Post
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib import messages


def index(request):
    posts = Post.objects.all()
    # categories = Category.objects.all()
    context = {
        "title": "Главная страница",
        "posts": posts,
        # "categories": categories
    }
    return render (request, 'cook/index.html', context)


def category_list(request, pk):
    posts = Post.objects.filter(category_id=pk)
    # categories = Category.objects.all()
    context = {
        "title": posts[0].category,
        "posts": posts,
        # "categories": categories
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
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect( 'post_detail', post.pk)
    else:
        form = PostAddForm()
        
    context = {
        'form': form,
        'title': 'Добавить статью',
         
    }
    return render(request, 'cook/article_add_form.html', context)
   

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, message='Вы успешно прошли')
            return redirect('index')
    else:
        form = LoginForm()
        
    context ={
        'title': 'Авторизация пользователя',
        'form': form
    } 
    return render(request, 'cook/login_form.html', context)


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    else:
        form = RegistrationForm()
        
    context ={
        'title': 'Регистрация пользователя',
        'form': form
    } 
    return render(request, 'cook/register.html', context)
