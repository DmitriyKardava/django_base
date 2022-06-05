from collections import UserString
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from authapp.models import ShopUser
from mainapp.models import Product, Category
from adminapp.forms import (ShopUserAdminEditForm,
                            ShopUserAdminCreateForm,
                            ProductCategoryEditForm,
                            ProductEditForm
                            )


class UserList(ListView):
    template_name = 'adminapp/users.html'
    queryset = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                               '-is_staff', 'username')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/пользователи'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('admin:users')
    fields = '__all__'

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html' 
    success_url = reverse_lazy('admin:categories') 
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'пользователи/редактирование'
        return context


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/новый'
    if request.method == 'POST':
        user_form = ShopUserAdminCreateForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        user_form = ShopUserAdminCreateForm()

    content = {'title': title, 'update_form': user_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'
    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(
            request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'пользователи/удаление'
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('admin:users'))

    content = {'title': title, 'user_to_delete': user}
    return render(request, 'adminapp/user_delete.html', content)


class CategoryList(ListView):
    template_name = 'adminapp/categories.html'
    queryset = Category.objects.all()
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/категории'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'админка/новая категория'
    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {'title': title, 'update_form': category_form}
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'категории/редактирование'
    edit_category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(
            request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:categories'))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'категории/удаление'
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('admin:categories'))

    content = {'title': title, 'category_to_delete': category}
    return render(request, 'adminapp/category_delete.html', content)


class ProductList(ListView):
    template_name = 'adminapp/products.html'
    paginate_by = 3

    def get_queryset(self):
        return Product.objects.filter(category=self.kwargs['category_pk']).order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'админка/продукты'
        context['category'] = get_object_or_404(
            Category, pk=self.kwargs['category_pk'])
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)
    form = ProductEditForm(initial={'category': category})
    if request.method == "POST":
        form = ProductEditForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[category_pk]))

    return render(
        request, 'adminapp/product_update.html',
        context={
            'title': 'новый продукт',
            'category': category,
            'form': form
        }
    )


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    category = get_object_or_404(Category, pk=product.category.pk)
    form = ProductEditForm(instance=product)
    if request.method == "POST":
        form = ProductEditForm(
            instance=product, data=request.POST, files=request.FILES)
        form.category = category
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))

    return render(
        request, 'adminapp/product_update.html',
        context={
            'title': 'редактировать продукт',
            'product': product,
            'category': category,
            'form': form
        }
    )


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    product.is_active = False
    product.save()
    return HttpResponseRedirect(reverse('admin:products', args=[product.category.pk]))
