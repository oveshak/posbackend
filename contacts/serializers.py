from rest_framework import serializers

from users.models import Branch, Users
from users.serializers import BranchSerializer
from .models import Contact, Customer, CustomerGroup
from globalapp.serializers import GlobalSerializers

class CustomerGroupSerializer(GlobalSerializers):
    # Create/Update এ শুধু ID নেবে
    group_leader_user = serializers.PrimaryKeyRelatedField(
        queryset=Users.objects.all(),
        required=False,
        allow_null=True,
        write_only=True
    )

    class Meta:
        model = CustomerGroup
        fields = '__all__'

    def to_representation(self, instance):
        """Return full Users data for group_leader_user"""
        data = super().to_representation(instance)

        # এখানে Users এর পুরো serializer ব্যবহার করা হলো
        if instance.group_leader_user:
            from users.serializers import UsersSerializer  # import inside to avoid circular import
            data['group_leader_user'] = UsersSerializer(instance.group_leader_user).data
        else:
            data['group_leader_user'] = None

        return data


# from_branch_name = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())
#     to_branch_name = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

#     class Meta:
#         model = StockTransfer
#         fields = '__all__'

#     def to_representation(self, instance):
#         """Return full nested objects for branch fields."""
#         data = super().to_representation(instance)

#         if instance.from_branch_name:
#             data['from_branch_name'] = BranchSerializer(instance.from_branch_name).data
#         if instance.to_branch_name:
#             data['to_branch_name'] = BranchSerializer(instance.to_branch_name).data

#         return data
class ContactSerializer(GlobalSerializers):
    # Writeable ForeignKey
    customer_group = serializers.PrimaryKeyRelatedField(queryset=CustomerGroup.objects.all(), required=False, allow_null=True)
    branch_name = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Contact
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # Nested representation
        data['customer_group'] = CustomerGroupSerializer(instance.customer_group).data if instance.customer_group else None
        data['branch_name'] = BranchSerializer(instance.branch_name).data if instance.branch_name else None

        return data

class CustomerSerializer(GlobalSerializers):
    # Writable ForeignKey
    branch_name = serializers.PrimaryKeyRelatedField(
        queryset=Branch.objects.all(), required=False, allow_null=True
    )
    guarantor = serializers.PrimaryKeyRelatedField(
        queryset=Contact.objects.all(), required=False, allow_null=True
    )

    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)

        # 🔹 Branch full object
        if instance.branch_name:
            data['branch_name'] = BranchSerializer(instance.branch_name).data
        else:
            data['branch_name'] = None

        # 🔹 Guarantor full object
        if instance.guarantor:
            data['guarantor'] = ContactSerializer(instance.guarantor).data
        else:
            data['guarantor'] = None

        return data
