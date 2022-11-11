from django.contrib.auth.models import User
from django.db import models


class Cathegory(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(max_length=400, null=True)

    def __str__(self):
        return self.name


class Boardgame(models.Model):
    name = models.CharField(max_length=300)
    producer = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    issue_year = models.CharField(max_length=10)
    min_age_of_player = models.PositiveSmallIntegerField()
    min_number_of_players = models.PositiveSmallIntegerField()
    max_number_of_players = models.PositiveSmallIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cathegory = models.ForeignKey(Cathegory, on_delete=models.PROTECT, related_name='boardgame')
    image_url = models.CharField(max_length=200, null=True)
    how_to_play = models.TextField(max_length=2000, null=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} --- {self.time} --- {self.amount}'


class Order(models.Model):

    STATUS_CHOICES = (
        (0, 'created'),
        (1, 'payed'),
        (2, 'delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # items = models.ManyToManyField(OrderItem, related_name='orders')
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=0)
    amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} --- {self.creation_time} --- {self.amount} --- {self.status}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Boardgame, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.order} --- {self.producte} --- {self.quantity} --- {self.price}'
