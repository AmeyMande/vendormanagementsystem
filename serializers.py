from rest_framework import serializers
from api.models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields='__all__'

class VendorPerformanceMetrixSerializer(serializers.Serializer):
    class Meta:
        model=VendorPerformanceRecord
        fields='__all__'