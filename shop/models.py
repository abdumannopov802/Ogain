from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/', blank=False)
    description = models.TextField(max_length=500, blank=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='products/', blank=False)
    sale = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    expired_date = models.DateField(blank=False)

    def __str__(self):
        return self.name

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.customer

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class StoreStaff(models.Model):
    MANAGER = 'manager'
    OPERATOR = 'operator'
    WORKER = 'worker'
    STATUS_CHOICES = [
        (MANAGER, 'Manager'),
        (OPERATOR, 'Operator'),
        (WORKER, 'Worker'),
    ]

    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    username = models.CharField(max_length=30, blank=False, unique=True)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} --> status: {self.status}"
