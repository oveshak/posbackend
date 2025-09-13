from rest_framework import serializers

from contacts.models import Contact, Customer
from contacts.serializers import ContactSerializer, CustomerSerializer
from products.models import Product
from products.serializers import ProductSerializer
from users.models import Branch, Users
from users.serializers import BranchSerializer, UsersSerializer
from .models import Purchase, PurchaseItem, PurchaseReturn, Sale, SaleItem, Payment, Cheque, AffiliateCommission,LoanType, InstallmentType, Installment, Loan
from globalapp.serializers import GlobalSerializers



class PurchaseSerializer(GlobalSerializers):
    # Writeable fields for POST/PUT
    supplier_name = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), allow_null=True)
    branch_name = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), allow_null=True)

    class Meta:
        model = Purchase
        fields = '__all__'

    def to_representation(self, instance):
        """Return full nested objects for supplier and branch"""
        data = super().to_representation(instance)

        if instance.supplier_name:
            data['supplier_name'] = ContactSerializer(instance.supplier_name).data
        if instance.branch_name:
            data['branch_name'] = BranchSerializer(instance.branch_name).data

        return data


class PurchaseItemSerializer(GlobalSerializers):
    # Writeable fields for POST/PUT
    product_name = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    purchase_name = serializers.PrimaryKeyRelatedField(queryset=Purchase.objects.all())

    class Meta:
        model = PurchaseItem
        fields = '__all__'

    def to_representation(self, instance):
        """Return full nested product and purchase objects"""
        data = super().to_representation(instance)

        if instance.product_name:
            data['product_name'] = ProductSerializer(instance.product_name).data
        if instance.purchase_name:
            data['purchase_name'] = PurchaseSerializer(instance.purchase_name).data

        return data


class PurchaseReturnSerializer(GlobalSerializers):
    class Meta:
        model = PurchaseReturn
        fields = '__all__'

# class SaleItemSerializer(GlobalSerializers):
#     product_name = serializers.CharField(source='product.name', read_only=True)
#     class Meta:
#         model = SaleItem
#         fields = '__all__'
class SaleItemSerializer(GlobalSerializers):
    # Writeable field for POST/PUT
    product_name = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all()
    )

    class Meta:
        model = SaleItem
        fields = '__all__'

    def to_representation(self, instance):
        """Return full nested product object instead of just ID"""
        data = super().to_representation(instance)

        if instance.product_name:
            data['product_name'] = ProductSerializer(instance.product_name).data

        return data


# class SaleSerializer(GlobalSerializers):
#     items = SaleItemSerializer(many=True, read_only=True)
#     customer_name = serializers.CharField(source='customer.name', read_only=True)
#     branch_name = serializers.CharField(source='branch.name', read_only=True)
#     supervisor_name = serializers.CharField(source='supervisor_user.name', read_only=True)
#     manager_name = serializers.CharField(source='manager_user.name', read_only=True)
#     class Meta:
#         model = Sale
#         fields = '__all__'

class SaleSerializer(GlobalSerializers):
    # Nested items
    items = SaleItemSerializer(many=True, read_only=True)

    # Writeable fields
    customer_name = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all()
    )
    branch_name = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all()
    )
    supervisor_user_name = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        allow_null=True,
        required=False
    )
    manager_user_name = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Sale
        fields = '__all__'

    def to_representation(self, instance):
        """
        Replace ForeignKey IDs with full nested objects in response
        """
        data = super().to_representation(instance)

        # Expand nested objects
        if instance.customer_name:
            data['customer_name'] = ContactSerializer(instance.customer_name).data
        if instance.branch_name:
            data['branch_name'] = BranchSerializer(instance.branch_name).data
        if instance.supervisor_user_name:
            data['supervisor_user_name'] = UsersSerializer(instance.supervisor_user_name).data
        if instance.manager_user_name:
            data['manager_user_name'] = UsersSerializer(instance.manager_user_name).data

        return data


# class PaymentSerializer(GlobalSerializers):
#     customer_name = serializers.CharField(source='customer.name', read_only=True)
#     class Meta:
#         model = Payment
#         fields = '__all__'

# class ChequeSerializer(GlobalSerializers):
#     customer_name = serializers.CharField(source='customer.name', read_only=True)
#     class Meta:
#         model = Cheque
#         fields = '__all__'

# class AffiliateCommissionSerializer(GlobalSerializers):
#     affiliate_user_name = serializers.CharField(source='affiliate_user.name', read_only=True)
#     class Meta:
#         model = AffiliateCommission
#         fields = '__all__'


# ---------------- Payment ----------------
class PaymentSerializer(GlobalSerializers):
    customer_name = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all()
    )
    sale_name = serializers.PrimaryKeyRelatedField(
        queryset=Sale.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Payment
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.customer_name:
            data['customer_name'] = ContactSerializer(instance.customer_name).data
        if instance.sale_name:
            data['sale_name'] = SaleSerializer(instance.sale_name).data
        return data


# ---------------- Cheque ----------------
class ChequeSerializer(GlobalSerializers):
    customer_name = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all()
    )
    loan_name = serializers.PrimaryKeyRelatedField(
        queryset=Sale.objects.all(),
        allow_null=True,
        required=False
    )

    class Meta:
        model = Cheque
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.customer_name:
            data['customer_name'] = ContactSerializer(instance.customer_name).data
        if instance.loan_name:
            data['loan_name'] = SaleSerializer(instance.loan_name).data
        return data


# ---------------- Affiliate Commission ----------------
class AffiliateCommissionSerializer(GlobalSerializers):
    affiliate_user_name = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all()
    )
    sale_name = serializers.PrimaryKeyRelatedField(
        queryset=Sale.objects.all()
    )

    class Meta:
        model = AffiliateCommission
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.affiliate_user_name:
            data['affiliate_user_name'] = UsersSerializer(instance.affiliate_user_name).data
        if instance.sale_name:
            data['sale_name'] = SaleSerializer(instance.sale_name).data
        return data



class LoanTypeSerializer(GlobalSerializers):
    class Meta:
        model = LoanType
        fields = '__all__'


class InstallmentTypeSerializer(GlobalSerializers):
    class Meta:
        model = InstallmentType
        fields = '__all__'


class InstallmentSerializer(GlobalSerializers):
    customer_name = serializers.CharField(source='customer.full_name', read_only=True)
    received_by_name = serializers.CharField(source='received_by.username', read_only=True)

    class Meta:
        model = Installment
        fields = '__all__'


class LoanSerializer(GlobalSerializers):
    customer_name_display = serializers.CharField(source='customer_name.full_name', read_only=True)
    loan_type_name = serializers.CharField(source='loan_type.name', read_only=True)
    installment_type_name = serializers.CharField(source='installment_type.type', read_only=True)
    installments = InstallmentSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = '__all__'

# ---------------- Installment ----------------
# class InstallmentSerializer(GlobalSerializers):
#     customer_name = serializers.PrimaryKeyRelatedField(
#         queryset=Customer.objects.all()
#     )
#     received_by = serializers.PrimaryKeyRelatedField(
#         queryset=Users.objects.all(),
#         allow_null=True,
#         required=False
#     )

#     class Meta:
#         model = Installment
#         fields = '__all__'

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         if instance.customer_name:
#             data['customer_name'] = CustomerSerializer(instance.customer_name).data
#         if instance.received_by:
#             data['received_by'] = UsersSerializer(instance.received_by).data
#         return data


# # ---------------- Loan ----------------
# class LoanSerializer(GlobalSerializers):
#     customer_name = serializers.PrimaryKeyRelatedField(
#         queryset=Customer.objects.all()
#     )
#     loan_type = serializers.PrimaryKeyRelatedField(
#         queryset=LoanType.objects.all(),
#         allow_null=True,
#         required=False
#     )
#     installment_type = serializers.PrimaryKeyRelatedField(
#         queryset=InstallmentType.objects.all(),
#         allow_null=True,
#         required=False
#     )
#     installment = InstallmentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Loan
#         fields = '__all__'

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         if instance.customer_name:
#             data['customer_name'] = CustomerSerializer(instance.customer_name).data
#         if instance.loan_type:
#             data['loan_type'] = LoanTypeSerializer(instance.loan_type).data
#         if instance.installment_type:
#             data['installment_type'] = InstallmentTypeSerializer(instance.installment_type).data
#         # Already handled installments via nested serializer
#         return data

