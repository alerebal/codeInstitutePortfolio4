"""restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from management.views import (reservation_form_view, home, edit_reservation,
                              delete_reservation, display_menu)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/<user_email>/', home, name='user_home'),
    path('reservation_form/', reservation_form_view, name='reservation_form'),
    path('edit_reservation/<reservation_id>/<new_time>', edit_reservation,
         name='edit_reservation'),
    path('delete_reservation/<reservation_id>', delete_reservation,
         name='delete_reservation'),
    path('display_menu/<kind>', display_menu, name='display_menu'),
]
