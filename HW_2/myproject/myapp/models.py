from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Name: {self.name}, '
                f'email: {self.email}, '
                f'phone_number: {self.phone_number}, '
                f'address: {self.address}, '
                f'registration_date: {self.registration_date}'
                )


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_count = models.IntegerField()
    product_added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'Name: {self.name}, '
                f'description: {self.description}, '
                f'price: {self.price}, '
                f'product_count: {self.product_count}, '
                f'product_added_date: {self.product_added_date}'
                )


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ №{self.id} создан!'
