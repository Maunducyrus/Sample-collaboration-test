"""
URL configuration for pharmacy11 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# from django.conf.urls import url, include


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^pharma/', include('pharma.urls')),
#     url(r'^$', views.home, name='index'),
# ]
from django.urls import path, include, re_path
from django.contrib import admin
from application import views
urlpatterns = [
    path('admin/', admin.site.urls),  # Simple path for admin
    path('application/', include('application.urls')),  # Simple path for pharma app URLs
    # path('', views.home, name='index'),
]
