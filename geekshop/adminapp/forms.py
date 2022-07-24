from django import forms
from authapp.models import ShopUser
from django.forms.widgets import HiddenInput
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from mainapp.models import Category, Product

class ShopUserAdminEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = '__all__'


class ShopUserAdminCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'avatar', 'age')


class ProductCategoryEditForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].widget = HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
