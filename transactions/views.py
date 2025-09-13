from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, authentication
from globalapp.views import BaseViews
from .models import Installment, InstallmentType, Loan, LoanType, Purchase, PurchaseItem, PurchaseReturn, Sale, SaleItem, Payment, Cheque, AffiliateCommission
from .serializers import (
    InstallmentSerializer, InstallmentTypeSerializer, LoanSerializer, LoanTypeSerializer, PurchaseSerializer, PurchaseItemSerializer, PurchaseReturnSerializer, SaleSerializer,
    SaleItemSerializer, PaymentSerializer, ChequeSerializer, AffiliateCommissionSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
class PurchaseViewSet(BaseViews):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Purchase
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class PurchaseItemViewSet(BaseViews):
    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = PurchaseItem
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class PurchaseReturnViewSet(BaseViews):
    queryset = PurchaseReturn.objects.all()
    serializer_class = PurchaseReturnSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = PurchaseReturn
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class SaleViewSet(BaseViews):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Sale
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class SaleItemViewSet(BaseViews):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = SaleItem
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class PaymentViewSet(BaseViews):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Payment
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class ChequeViewSet(BaseViews):
    queryset = Cheque.objects.all()
    serializer_class = ChequeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Cheque
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class AffiliateCommissionViewSet(BaseViews):
    queryset = AffiliateCommission.objects.all()
    serializer_class = AffiliateCommissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = AffiliateCommission
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class LoanTypeViewSet(BaseViews):
    queryset = LoanType.objects.all()
    serializer_class = LoanTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = LoanType
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy"]


class InstallmentTypeViewSet(BaseViews):
    queryset = InstallmentType.objects.all()
    serializer_class = InstallmentTypeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = InstallmentType
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy"]


class InstallmentViewSet(BaseViews):
    queryset = Installment.objects.all()
    serializer_class = InstallmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Installment
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy"]

class LoanViewSet(BaseViews):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Loan
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy"]

    
   