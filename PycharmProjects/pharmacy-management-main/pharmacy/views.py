# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect, HttpResponse
# from django.shortcuts import render, redirect
#
# from django.contrib import messages
# from .decorators import *
#
# # Create your views here.
#
# @unautheticated_user
# def loginPage(request):
#
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#
#         user=authenticate(request,username=username,password=password)
#         if user != None:
#             login(request, user)
#             user_type = user.user_type
#             if user_type == '1':
#                 return redirect('/')
#
#             elif user_type == '2':
#                 return redirect('pharmacist_home')
#
#             elif user_type == '3':
#                 return redirect('doctor_home')
#             elif user_type == '4':
#                 return redirect('clerk_home')
#             elif user_type == '5':
#                 return redirect('patient_home')
#
#
#             else:
#                 messages.error(request, "Invalid Login!")
#                 return redirect('login')
#         else:
#             messages.error(request, "Invalid Login Credentials!")
#             return redirect('login')
#
#     return render(request,'login.html')
#
#
#
# def logoutUser(request):
#     logout(request)
#     return redirect('login')

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import *  # Corrected the decorator name


# Create your views here.

@unauthenticated_user  # Corrected the decorator name
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)

            # Redirect based on user_type
            user_type = user.user_type  # Assuming 'user_type' is a field in your User model
            if user_type == '1':  # Admin
                return redirect('admin_dashboard')  # Corrected the redirect path for the admin

            elif user_type == '2':  # Pharmacist
                return redirect('pharmacist_home')

            elif user_type == '3':  # Doctor
                return redirect('doctor_home')

            elif user_type == '4':  # Clerk
                return redirect('clerk_home')

            elif user_type == '5':  # Patient
                return redirect('patient_home')

            else:
                messages.error(request, "Invalid User Type!")
                return redirect('login')
        else:
            messages.error(request, "Invalid Login Credentials!")
            return redirect('login')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to login page after logout

