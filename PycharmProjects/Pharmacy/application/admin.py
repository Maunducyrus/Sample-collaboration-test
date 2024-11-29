from django.contrib import admin
from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase

# Register your models here.

admin.site.register(Dealer)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Medicine)
admin.site.register(Purchase)

