from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    path("", Index.as_view(), name = 'index'),
    # path('category/<int:pk>/', category_list, name='category_list' ),
     path('category/<int:pk>/', Article_by_category.as_view(), name='category_list' ),
    # path('post/<int:pk>/', post_detail, name='post_detail' ),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail' ),
    # path('add_article', add_post, name='add'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name = 'post_delete'),
    path('search', SearchResults.as_view(), name = 'search'),
    path('add_article', AddPost.as_view(), name='add'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),
]
    
