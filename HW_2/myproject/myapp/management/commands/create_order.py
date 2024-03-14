from django.core.management.base import BaseCommand
from myapp.models import Order
from myapp.models import Product
from myapp.models import Client


class Command(BaseCommand):
    help = "Create order"

    def handle(self, *args, **kwargs):
        client = Client.objects.order_by('?').first()
        products = Product.objects.order_by('?')[:3]
        total_price = sum(product.price for product in products)
        order = Order(client=client,
                      total_price=total_price,
                      )
        order.save()
        order.products.set(products)
        self.stdout.write(f'{order}')
