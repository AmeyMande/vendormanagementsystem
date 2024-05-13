from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display=['id','name','contact_details','address','vendor_code']

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display=['po_number','vendor','order_date','delivery_date','items','quantity']

@admin.register(VendorPerformanceRecord)
class VendorPerformanceAdmin(admin.ModelAdmin):
    list_display=['vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']
