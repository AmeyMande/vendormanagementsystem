from .models import *
from .serializers import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView,RetrieveAPIView

# Create your views here.
class VendorListCreate(ListCreateAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class VendorRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Vendor.objects.all()
    serializer_class=VendorSerializer

class PurchaseOrderListCreate(ListCreateAPIView):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=PurchaseOrder.objects.all()
    serializer_class=PurchaseOrderSerializer

class VendorPerformanceRetrieveAPIView(RetrieveAPIView):
    queryset = VendorPerformanceRecord.objects.all()
    serializer_class = VendorPerformanceMetrixSerializer

