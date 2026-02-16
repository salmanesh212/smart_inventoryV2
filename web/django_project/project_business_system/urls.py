"""
URL configuration for project_business_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from business_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('create_product/', views.product_Create, name='create_product'),
    path('product/<int:product_id>/', views.product_read, name='product_read'),
    path('update_product/<int:NewProductid>/', views.product_update, name='product_update'),
    path('delete_product/<int:product_id>/', views.product_delete, name='product_delete'),
    path('register_customer/', views.customer_registration, name='register_customer'),
    path('create_order/', views.create_order, name='create_order'),
    path('display_orders/', views.display_orders, name='display_orders'),
    path('products/', views.list_products, name='product_list'),
    path('analytics/', views.analytics_dashboard, name='analytics_dashboard'),
]
