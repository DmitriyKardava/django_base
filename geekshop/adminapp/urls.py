from unicodedata import category
import adminapp.views as adminapp
from django.urls import path
app_name = 'adminapp'
urlpatterns = [
    path('users/', adminapp.UserList.as_view(), name='users'),
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/update/<int:pk>/',
         adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/',
         adminapp.UserDleteView.as_view(), name='user_delete'),

    path('categories/', adminapp.CategoryList.as_view(), name='categories'),
    path('categories/create/', adminapp.CategoryCreateView.as_view(),
         name='category_create'),
    path('categories/update/<int:pk>/',
         adminapp.CategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/',
         adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    path('products/<int:category_pk>/',adminapp.products, name='products'),
    path('products/<int:category_pk>/create/',adminapp.product_create, name='product_create'),
    path('products/update/<int:product_pk>/',adminapp.product_update, name='product_update'),
    path('products/delete/<int:product_pk>/',adminapp.product_delete, name='product_delete'),
  ]
