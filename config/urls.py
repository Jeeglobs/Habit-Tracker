"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),

    path('', views.list_habits, name='home'),

    path('add-habit', views.add_habit, name='add_habit'),
    path('edit-habit/<int:pk>', views.edit_habit, name='edit_habit'),
    path('delete-habit/<int:pk>', views.delete_habit, name='delete_habit'),
    path('habit-details/<int:pk>', views.view_habit_details,
         name='habit_details'),

    path('add-record/<int:pk>', views.add_record, name='add_record'),
    path('edit-record/<int:pk>', views.edit_record, name='edit_record'),
    path('delete-record<int:pk>', views.delete_record, name='delete_record'),
    path('record-details/<int:pk>', views.view_record_details,
         name='record_details'),
]
