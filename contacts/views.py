from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, authentication
from globalapp.views import BaseViews
from .models import Contact, Customer, CustomerGroup
from .serializers import ContactSerializer, CustomerGroupSerializer, CustomerSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
class CustomerGroupViewSet(BaseViews):
    queryset = CustomerGroup.objects.all()
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]
    serializer_class = CustomerGroupSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = CustomerGroup

class ContactViewSet(BaseViews):
    queryset = Contact.objects.all()
    methods = ["list", "retrieve", "create", "update", "partial_update", "destroy", "soft_delete", "change_status", "restore_soft_deleted"]
    serializer_class = ContactSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Contact

class CustomerViewSet(BaseViews):
    queryset = Customer.objects.all()
    methods = [
        "list",
        "retrieve",
        "create",
        "update",
        "partial_update",
        "destroy",
        "soft_delete",
        "change_status",
        "restore_soft_deleted"
    ]
    serializer_class = CustomerSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    model_name = Customer