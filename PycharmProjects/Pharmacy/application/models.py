from django.db import models

# Create your models here.
class Dealer(models.Model):
    dname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField(unique=True)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Employee(models.Model):
    e_id = models.IntegerField(unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    sal = models.CharField(max_length=20)
    phn_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email


class Medicine(models.Model):
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=50)
    dname = models.CharField(max_length=50)
    desc = models.CharField(max_length=10)
    price = models.CharField(max_length=30)
    stock = models.IntegerField()

    def __str__(self):
        return self.mname


class Purchase(models.Model):
    pname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phn_no = models.BigIntegerField()
    price = models.IntegerField()
    qty = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.pname
