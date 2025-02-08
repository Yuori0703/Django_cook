from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from django.db.models import F, Q
from .forms import PostAddForm, LoginForm, RegistrationForm, CommentForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


# def index(request):
#     posts = Post.objects.all()
#     categories = Category.objects.all()
#     context = {
#         "title": "Главная страница",
#         "posts": posts,
#         "categories": categories
#     }
#     return render (request, 'cook/index.html', context)


class Index(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'cook/index.html'
    extra_context = {'title': "Главная страница"}
    
    

# def category_list(request, pk):
#     posts = Post.objects.filter(category_id=pk)
#     categories = Category.objects.all()
#     context = {
#         "title": posts[0].category,
#         "posts": posts,
#         "categories": categories
#     }
#     return render (request, 'cook/index.html', context)


class Article_by_category(Index):
    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['title'] = category.title
        return context



# def post_detail(request, pk):
#     article = Post.objects.get(pk=pk)
#     Post.objects.filter(pk=pk).update(wathed=F('wathed') + 1)
#     ext_post = Post.objects.all().order_by('-wathed')[:5]
#     context = { 
#                'title': article.title,
#                'post': article,
#                'ext_post': ext_post,
        
#     }
#     return render(request, 'cook/article_detail.html', context)


class PostDetail(DeleteView):
    model = Post
    template_name = 'cook/article_detail.html'
    
    def get_queryset(self):
        return Post.objects.filter(pk=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        Post.objects.filter(pk=self.kwargs['pk']).update(wathed=F('wathed') + 1)
        context = super().get_context_data()
        post = Post.objects.get(pk=self.kwargs['pk'])
        posts = Post.objects.all().exclude(pk=self.kwargs['pk']).order_by('-wathed')
        context['title'] = post.title
        context['ext_posts'] = posts
        if self.request.user.is_authenticated:
            context['comment_form'] = CommentForm
        return context
    


# def add_post(request):
#     if request.method == 'POST':
#         form = PostAddForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = Post.objects.create(**form.cleaned_data)
#             post.save()
#             return redirect( 'post_detail', post.pk)
#     else:
#         form = PostAddForm()
#     context = {
#         'form': form,
#         'title': 'Добавить статью',
#     }
#     return render(request, 'cook/article_add_form.html', context)


class AddPost(CreateView):
    form_class = PostAddForm
    template_name = 'cook/article_add_form.html'
    extra_context = {'title': 'Добавить статью'}
    
    
class PostUpdate(UpdateView):
    model = Post
    form_class = PostAddForm
    template_name = 'cook/article_add_form.html'
    extra_context = {'title': 'Изменение статьи'}
    
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'
       

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


class SearchResults(Index):
    
    def get_queryset(self):
        word = self.request.GET.get('q')
        posts = Post.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word)
        )
        return posts
    
    
def add_comment(request, post_id):
    form = CommentForm(data= request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = Post.objects.get(pk=post_id)
        comment.save()
        messages.success(request, "Ваш коментарий успешно добавлен")    
            
    return redirect('post_detail', post_id)
