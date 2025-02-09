from django.urls import path, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

    
schema_view = get_schema_view(
    openapi.Info(
        title='Главный дед мороз'б
        default_version="v 0.0.1",
        description="Документация по API к курсу кулинария",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email='example@mail.com'),
        license=openapi.License(name='BCD License')
    ),
    public=True,
    permission_classes=[permissions.Allowly, ],
)



urlpatterns = [
    # path('', index, name='index'),
    path("", Index.as_view(), name = 'index'),
    # path('category/<int:pk>/', category_list, name='category_list' ),
     path('category/<int:pk>/', ArticleByCategory.as_view(), name='category_list' ),
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
    path('profile/<int:user_id>', profile, name='profile'),
    path('password/', UserChangePassword.as_view(), name='change_password'),
    
    # API
    path("posts/api/", CookAPI.as_view(), name="CookAPI"),
    path("posts/api/<int:pk>", CookAPIDetail.as_view(), name="CookAPIDetail"),
    path("categories/api/", CookCategoryAPI.as_view(), name="CookCategoryAPI"),
    path("categories/api/<int:pk>", CookCategoryAPIDetail.as_view(), name="CookCategoryAPIDetail"),
    
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
]
    
