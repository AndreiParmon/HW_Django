from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Name{i}',
                              description=lorem_ipsum.words(10),
                              price=i + i,
                              product_count=i + i,
                              )
            product.save()
            self.stdout.write(f'{product}')
