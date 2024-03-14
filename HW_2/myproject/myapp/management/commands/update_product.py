from decimal import Decimal

from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Update product info by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=Decimal, help='Product price')
        parser.add_argument('product_count', type=int, help='Product product_count')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        product_count = kwargs.get('product_count')
        product = Product.objects.filter(pk=pk).first()
        product.name = name
        product.description = description
        product.price = price
        product.product_count = product_count
        product.save()
        self.stdout.write(f'{product}')
