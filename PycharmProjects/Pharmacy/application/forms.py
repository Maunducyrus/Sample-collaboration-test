from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['cust_id', 'fname', 'lname', 'phn_no', 'address', 'med_name', 'qty']