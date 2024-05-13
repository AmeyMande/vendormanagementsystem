"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/vendorapi/<int:pk>/',views.VendorRetrieveUpdateDelete.as_view()),
    path('api/vendorapi/',views.VendorListCreate.as_view()),
    path('api/purchase_orders/',views.PurchaseOrderListCreate.as_view()),
    path('api/purchase_orders/<int:pk>/',views.PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('api/vendors/<int:pk>/performance/', views.VendorPerformanceRetrieveAPIView.as_view()),
]
