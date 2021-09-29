
from django.contrib import admin
from django.urls import path
from apiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.student_api),
]
