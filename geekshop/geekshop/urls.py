"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('admin/', include('adminapp.urls', namespace='admin')),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('cart/', include('cartapp.urls', namespace='cart')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('products/<int:pk>/', mainapp.category, name='category'),
    path('products/all/', mainapp.products, name='products_all'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
for (name, item) in mainapp.main_menu.items():
    try:
        urlpatterns.append(
            path(item['url'], getattr(mainapp, name), name=name))
    except AttributeError:
        print(f'Не определено представление для {name}')

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
