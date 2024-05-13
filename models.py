from django.db import models
from django.db.models import Avg, Count,F
import datetime
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from .serializers import VendorSerializer,PurchaseOrderSerializer,VendorPerformanceMetrixSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.IntegerField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=5, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

STATUS = ((1, "pending"), (2, "completed"),(3,"caceled"))    
class PurchaseOrder(models.Model):
    po_number = models.IntegerField(unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.IntegerField(choices=STATUS,default=1)
    quality_rating = models.FloatField(default=0,null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number
    
@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    if created or instance.status != 'pending':
        vendor = instance.vendor

        completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_pos = completed_pos.count()

        #for ontimedeliveryrate
        on_time_deliveries = completed_pos.filter(delivery_date__lte=F('delivery_date')).count()
        on_time_delivery_rate = on_time_deliveries / total_completed_pos

        #for qualityratingaverage
        quality_rating_avg = completed_pos.aggregate(avg_quality_rating=models.Avg('quality_rating'))

        #for averageresponse
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() / 3600 for po in completed_pos if po.acknowledgment_date and po.issue_date]
        average_response_time = sum(response_times) / len(response_times)

        #for fullfillrate
        total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
        fulfilled_pos = completed_pos.filter(quality_rating__isnull=False).count()
        fulfillment_rate = fulfilled_pos / total_pos

        # Update vendor performance metrics
        VendorPerformanceRecord.on_time_delivery_rate = on_time_delivery_rate
        VendorPerformanceRecord.quality_rating_avg = quality_rating_avg
        VendorPerformanceRecord.average_response_time = average_response_time
        VendorPerformanceRecord.fulfillment_rate = fulfillment_rate
        VendorPerformanceRecord.save()
    
class VendorPerformanceRecord(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"
    
