from rest_framework import serializers
from .models import Contact, Customer, CustomerGroup
from globalapp.serializers import GlobalSerializers

class CustomerGroupSerializer(GlobalSerializers):
    class Meta:
        model = CustomerGroup
        fields = '__all__'

class ContactSerializer(GlobalSerializers):
    customer_group_name = serializers.CharField(source='customer_group.name', read_only=True)
    branch_name = serializers.CharField(source='branch.name', read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

class CustomerSerializer(GlobalSerializers):
    guarantor_name = serializers.CharField(source='guarantor.name', read_only=True)
    branch_name = serializers.CharField(source='branch_name.name', read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'