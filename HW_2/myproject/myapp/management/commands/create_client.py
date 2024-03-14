from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from myapp.models import Client


class Command(BaseCommand):
    help = "Create client"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'Name{i}',
                            email=f'mail{i}@mail.ru',
                            phone_number=f'phone_number +3753312345{i}',
                            address=lorem_ipsum.words(10),
                            )
            client.save()
            self.stdout.write(f'{client}')
