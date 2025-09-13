from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, authentication
from globalapp.views import BaseViews
from .models import Product, Unit, Category, Brand, Warranty, SellingPriceGroup, Variation, BranchProductStock
from .serializers import (
    ProductSerializer, UnitSerializer, CategorySerializer, BrandSerializer,
    WarrantySerializer, SellingPriceGroupSerializer, VariationSerializer,
    BranchProductStockSerializer
)
from rest_framework_simplejwt.authentication import JWTAuthentication
class UnitViewSet(BaseViews):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Unit
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class CategoryViewSet(BaseViews):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Category
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class BrandViewSet(BaseViews):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Brand
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class WarrantyViewSet(BaseViews):
    queryset = Warranty.objects.all()
    serializer_class = WarrantySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Warranty
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class SellingPriceGroupViewSet(BaseViews):
    queryset = SellingPriceGroup.objects.all()
    serializer_class = SellingPriceGroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = SellingPriceGroup
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class ProductViewSet(BaseViews):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Product
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class VariationViewSet(BaseViews):
    queryset = Variation.objects.all()
    serializer_class = VariationSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Variation
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]

class BranchProductStockViewSet(BaseViews):
    queryset = BranchProductStock.objects.all()
    serializer_class = BranchProductStockSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = BranchProductStock
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]
