
from django.db import models
from django.utils.timezone import now
from django.utils import timezone


class Inventory(models.Model):
    name = models.CharField(max_length=255)  # Medicine name
    description = models.TextField(blank=True, null=True)  # Optional description
    quantity = models.PositiveIntegerField(default=0)  # Current stock level
    reorder_level = models.PositiveIntegerField(default=10)  # Minimum stock before reorder
    expiry_date = models.DateField()  # Expiration date
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # Unit price
    created_at = models.DateTimeField(auto_now_add=True)  # Date added to inventory
    updated_at = models.DateTimeField(auto_now=True)  # Last updated

    def is_low_stock(self):
        return self.quantity < self.reorder_level

    def is_expired(self):
        return self.expiry_date < now().date()

    def __str__(self):
        return self.name


class Sale(models.Model):
    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)  # Item sold
    quantity_sold = models.PositiveIntegerField()  # Quantity sold
    # amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add default value
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)  # Correct use of timezone.now


    def __str__(self):
        return f"Sale of {self.inventory_item.name} on {self.date.strftime('%Y-%m-%d')}"

    @property
    def total_cost(self):
        return self.quantity_sold * self.inventory_item.price_per_unit

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    inventory_item = models.ForeignKey(Inventory, on_delete=models.CASCADE)  # Item ordered
    quantity_ordered = models.PositiveIntegerField()  # Quantity ordered
    order_date = models.DateTimeField(auto_now_add=True)  # Date and time of the order
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')  # Order status
    supplier = models.CharField(max_length=255, blank=True, null=True)  # Supplier information (if applicable)

    def __str__(self):
        return f"Order of {self.inventory_item.name} - {self.status}"
