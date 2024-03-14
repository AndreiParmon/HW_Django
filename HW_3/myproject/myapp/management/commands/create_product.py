from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        product = Product(name='Philips',
                          price=800,
                          description='TV panel',
                          product_count=1,
                          )
        product.save()
        self.stdout.write(f'{product}')
