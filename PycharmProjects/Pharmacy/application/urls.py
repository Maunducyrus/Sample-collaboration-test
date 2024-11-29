# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     url(r'^$', views.home, name='index'),
#
#     url(r'^dealerform/', views.dealerform, name="dealerform"),
#     url(r'^dealerforminsert/', views.dealerforminsert, name="dealerforminsert"),
#     url(r'^dealerformupdate(?P<foo>[0-9]+)/', views.dealerformupdate, name="dealerformupdate"),
#     url(r'^dealerformview(?P<foo>[0-9]+)/', views.dealerformview, name="dealerformview"),
#     url(r'^dealerformdelete(?P<foo>[0-9]+)/', views.dealerformdelete, name="dealerformdelete"),
#     url(r'^dealertable/', views.dealertable, name='dealertable'),
#
#     url(r'^medform/', views.medform, name="medform"),
#     url(r'^medforminsert/', views.medforminsert, name="medforminsert"),
#     url(r'^medformupdate(?P<foo>[0-9]+)/', views.medformupdate, name="medformupdate"),
#     url(r'^medformview(?P<foo>[0-9]+)/', views.medformview, name="medformview"),
#     url(r'^medformdelete(?P<foo>[0-9]+)/', views.medformdelete, name="medformdelete"),
#     url(r'^medtable/', views.medtable, name='medtable'),
#
#     url(r'^empform/', views.empform, name="empform"),
#     url(r'^empforminsert/', views.empforminsert, name="empforminsert"),
#     url(r'^empformupdate(?P<foo>[0-9]+)/', views.empformupdate, name="empformupdate"),
#     url(r'^empformview(?P<foo>[0-9]+)/', views.empformview, name="empformview"),
#     url(r'^empformdelete(?P<foo>[0-9]+)/', views.empformdelete, name="empformdelete"),
#     url(r'^emptable/', views.emptable, name='emptable'),
#
#     url(r'^custform/', views.custform, name="custform"),
#     url(r'^custforminsert/', views.custforminsert, name="custforminsert"),
#     url(r'^custformupdate(?P<foo>[0-9]+)/', views.custformupdate, name="custformupdate"),
#     url(r'^custformview(?P<foo>[0-9]+)/', views.custformview, name="custformview"),
#     url(r'^custformdelete(?P<foo>[0-9]+)/', views.custformdelete, name="custformdelete"),
#     url(r'^custtable/', views.custtable, name='custtable'),
#
#     url(r'^purchaseform/', views.purchaseform, name="purchaseform"),
#     url(r'^purchaseforminsert/', views.purchaseforminsert, name="purchaseforminsert"),
#     url(r'^purchaseformupdate(?P<foo>[0-9]+)/', views.purchaseformupdate, name="purchaseformupdate"),
#     url(r'^purchaseformview(?P<foo>[0-9]+)/', views.purchaseformview, name="purchaseformview"),
#     url(r'^purchaseformdelete(?P<foo>[0-9]+)/', views.purchaseformdelete, name="purchaseformdelete"),
#     url(r'^purchasetable/', views.purchasetable, name='purchasetable')
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Dealer URLs
    path('dealers/', views.DealerListView.as_view(), name='dealer_list'),
    path('dealer/new/', views.DealerCreateView.as_view(), name='dealer_create'),
    path('dealer/<int:pk>/edit/', views.DealerUpdateView.as_view(), name='dealer_update'),
    path('dealer/<int:pk>/delete/', views.DealerDeleteView.as_view(), name='dealer_delete'),

    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/new/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employee/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Customer URLs
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/new/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('customer/<int:pk>/edit/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/<int:pk>/delete/', views.CustomerDeleteView.as_view(), name='customer_delete'),

    # Medicine URLs
    path('medicines/', views.MedicineListView.as_view(), name='medicine_list'),
    path('medicine/new/', views.MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/edit/', views.MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', views.MedicineDeleteView.as_view(), name='medicine_delete'),

    # Purchase URLs
    path('purchases/', views.PurchaseListView.as_view(), name='purchase_list'),
    path('purchase/new/', views.PurchaseCreateView.as_view(), name='purchase_create'),
    path('purchase/<int:pk>/edit/', views.PurchaseUpdateView.as_view(), name='purchase_update'),
    path('purchase/<int:pk>/delete/', views.PurchaseDeleteView.as_view(), name='purchase_delete'),
]
