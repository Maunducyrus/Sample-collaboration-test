#
# # Create your views here.
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from .models import Inventory, Sale, Order
from django.utils.timezone import now
from django.db.models import Sum

def home(request):
    return render(request, 'home.html')


@login_required
# @user_passes_test(is_admin)
def dashboard(request):
    # Calculate total sales for today
    today = now().date()
    total_sales = Sale.objects.filter(date__date=today).aggregate(total=Sum('amount'))['total'] or 0

    # Count low stock items
    low_stock_count = Inventory.objects.filter(quantity__lt=10).count()

    # Count expired items
    expired_items = Inventory.objects.filter(expiry_date__lt=today).count()

    # Count pending orders
    pending_orders = Order.objects.filter(status='Pending').count()

    context = {
        'total_sales': total_sales,
        'low_stock_count': low_stock_count,
        'expired_items': expired_items,
        'pending_orders': pending_orders,
    }
    return render(request, 'dashboard.html', context)

