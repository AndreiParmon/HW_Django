from django.core.management.base import BaseCommand
from myapp.models import Order
from myapp.models import Product
from myapp.models import Client


class Command(BaseCommand):
    help = "Update order"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='ID of the order to update')
        parser.add_argument('client_id', type=int, help='ID of the new client')
        parser.add_argument('product_ID', type=int, nargs='+', help='ID of the products to add to the order')

    def handle(self, *args, **kwargs):
        total_price = 0
        order_id = kwargs['order_id']
        client_id = kwargs['client_id']
        product_ID = kwargs['product_ID']

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Order with ID {order_id} does not exist'))
            return
        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Customer with ID {client_id} does not exist'))
            return

        order.client = client

        order.products.clear()
        for product_id in product_ID:
            try:
                product = Product.objects.get(pk=product_id)
                order.products.add(product)
                total_price += product.price
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist'))
                return
        order.total_price = total_price
        order.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully updated order: {order}'))
