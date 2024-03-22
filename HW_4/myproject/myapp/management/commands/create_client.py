from django.core.management.base import BaseCommand
from myapp.models import Client


class Command(BaseCommand):
    help = "Create client"

    def handle(self, *args, **kwargs):
        client = Client(name='Andrei',
                        email='andrei@example.com',
                        phone_number='375336363146',
                        address='Belarus',
                        )
        client.save()
        self.stdout.write(f'{client}')
