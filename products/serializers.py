from rest_framework import serializers

from users.models import Branch
from users.serializers import BranchSerializer
from .models import Product, Unit, Category, Brand, Warranty, SellingPriceGroup, Variation, BranchProductStock
from globalapp.serializers import GlobalSerializers

class UnitSerializer(GlobalSerializers):
    class Meta:
        model = Unit
        fields = '__all__'

class CategorySerializer(GlobalSerializers):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(GlobalSerializers):
    class Meta:
        model = Brand
        fields = '__all__'

class WarrantySerializer(GlobalSerializers):
    class Meta:
        model = Warranty
        fields = '__all__'

class SellingPriceGroupSerializer(GlobalSerializers):
    class Meta:
        model = SellingPriceGroup
        fields = '__all__'


        
class VariationSerializer(GlobalSerializers):
    # Writeable field for POST/PUT
    product_name = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = Variation
        fields = '__all__'

    def to_representation(self, instance):
        """Return full nested product object instead of just ID"""
        data = super().to_representation(instance)

        if instance.product_name:
            data['product_name'] = ProductSerializer(instance.product_name).data

        return data
    

    
# class ProductSerializer(GlobalSerializers):
#     unit_name = serializers.CharField(source='unit.name', read_only=True)
#     category_name = serializers.CharField(source='category.name', read_only=True)
#     brand_name = serializers.CharField(source='brand.name', read_only=True)
#     warranty_name = serializers.CharField(source='warranty.name', read_only=True)
#     variations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

#     class Meta:
#         model = Product
#         fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    unit_name_data = serializers.CharField(source='unit_name.name', read_only=True)
    category_name_data = serializers.CharField(source='category_name.name', read_only=True)
    brand_name_data = serializers.CharField(source='brand_name.name', read_only=True)
    warranty_name_data = serializers.CharField(source='warranty_name.name', read_only=True)

    unit_name = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), allow_null=True)
    category_name = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), allow_null=True)
    brand_name = serializers.PrimaryKeyRelatedField(queryset=Brand.objects.all(), allow_null=True)
    warranty_name = serializers.PrimaryKeyRelatedField(queryset=Warranty.objects.all(), allow_null=True)

    class Meta:
        model = Product
        fields = '__all__'


# class VariationSerializer(GlobalSerializers):
#     class Meta:
#         model = Variation
#         fields = '__all__'



class BranchProductStockSerializer(GlobalSerializers):
    # Writeable fields for POST/PUT
    product_name = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    branch_name = serializers.PrimaryKeyRelatedField(queryset=Branch.objects.all())

    class Meta:
        model = BranchProductStock
        fields = '__all__'

    def to_representation(self, instance):
        """Return full nested product and branch objects"""
        data = super().to_representation(instance)

        if instance.product_name:
            data['product_name'] = ProductSerializer(instance.product_name).data
        if instance.branch_name:
            data['branch_name'] = BranchSerializer(instance.branch_name).data

        return data