from django.db import models
from django.contrib.auth.models import User
markup = 0.25


def price(cost):
    """
    Takes in a cost and returns the marked up price of the item.
    """
    increase = markup * cost
    actual_cost = increase + cost
    return actual_cost


# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
)


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    product_id = models.CharField(max_length=25)
    cost = models.FloatField()
    quantity = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return f'{self.name} | {self.product_id} | {self.cost} | {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} requested by {self.staff.username} on the date of {self.date}'
