from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),  # Главная страница с товарами  edit
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('postlist', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
     path('post/new/', views.post_new, name='post_new'),
     path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]