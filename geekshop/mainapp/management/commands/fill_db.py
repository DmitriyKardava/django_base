from django.core.management import BaseCommand
from mainapp.models import Category, Product
from authapp.models import ShopUser

import os
import json

JSON_PATH = os.path.join('mainapp', 'json')


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name+'.json'), 'r') as in_file:
        return json.load(in_file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            product['category'] = Category.objects.get(
                name=product['category'])
            new_product = Product(**product)
            new_product.save()

    admin_name = 'shopadmin'
    if not ShopUser.objects.filter(username=admin_name):
        super_user = ShopUser.objects.create_superuser(
            admin_name, 'admin@localhost', '1234')
    else:
        super_user = ShopUser.objects.get(username=admin_name)
        super_user.is_superuser = True
        super_user.set_password = '1234'
        super_user.save()
