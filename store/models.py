from django.db import models
import datetime


class Product(models.Model):
    sku = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(default="", max_length=255, blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="uploads/product/")

    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=30, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
