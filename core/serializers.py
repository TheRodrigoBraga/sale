from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from core import models


class SerializerBase(FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super(SerializerBase, self).get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class ZoneSerializer(SerializerBase):
    class Meta:
        model = models.Zone
        fields = '__all__'


class StateSerializer(SerializerBase):
    class Meta:
        model = models.State
        fields = '__all__'


class CitySerializer(SerializerBase):
    class Meta:
        model = models.City
        fields = '__all__'

    expandable_fields = {
        'state': (
            'core.StateSerializer',
            {'source': 'state', 'fields': ['id', 'url', 'name']}
        )
    }


class DistrictSerializer(SerializerBase):
    class Meta:
        model = models.District
        fields = '__all__'

    expandable_fields = {
        'city': (
            'core.CitySerializer',
            {'source': 'city', 'fields': ['id', 'url', 'name']}
        ),
        'zone': (
            'core.ZoneSerializer',
            {'source': 'zone', 'fields': ['id', 'url', 'name']}
        )
    }


class SupplierSerializer(SerializerBase):
    class Meta:
        model = models.Supplier
        fields = '__all__'


class ProductGroupSerializer(SerializerBase):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductSerializer(SerializerBase):
    class Meta:
        model = models.Product
        fields = '__all__'

    expandable_fields = {
        'product_group': (
            'core.ProductGroupSerializer',
            {'source': 'product_group', 'fields': ['id', 'url', 'name']}
        ),
        'supplier': (
            'core.SupplierSerializer',
            {'source': 'supplier', 'fields': ['id', 'url', 'name']}
        )
    }


class BranchSerializer(SerializerBase):
    class Meta:
        model = models.Branch
        fields = '__all__'

    expandable_fields = {
        'district': (
            'core.DistrictSerializer',
            {'source': 'district', 'fields': ['id', 'url', 'name']}
        )
    }


class DepartmentSerializer(SerializerBase):
    class Meta:
        model = models.Department
        fields = '__all__'


class MaritalStatusSerializer(SerializerBase):
    class Meta:
        model = models.MaritalStatus
        fields = '__all__'


class EmployeeSerializer(SerializerBase):
    class Meta:
        model = models.Employee
        fields = '__all__'

    expandable_fields = {
        'department': (
            'core.DepartmentSerializer',
            {'source': 'department', 'fields': ['id', 'url', 'name']}
        ),
        'district': (
            'core.DistrictSerializer',
            {'source': 'district', 'fields': ['id', 'url', 'name']}
        ),
        'marital_status': (
            'core.MaritalStatusSerializer',
            {'source': 'marital_status', 'fields': ['id', 'url', 'name']}
        )
    }


class CustomerSerializer(SerializerBase):
    class Meta:
        model = models.Customer
        fields = '__all__'

    expandable_fields = {
        'district': (
            'core.DistrictSerializer',
            {'source': 'district', 'fields': ['id', 'url', 'name']}
        ),
        'marital_status': (
            'core.MaritalStatusSerializer',
            {'source': 'marital_status', 'fields': ['id', 'url', 'name']}
        )
    }


class SaleSerializer(SerializerBase):
    class Meta:
        model = models.Sale
        fields = '__all__'

    expandable_fields = {
        'customer': (
            'core.CustomerSerializer',
            {'source': 'customer', 'fields': ['id', 'url', 'name']}
        ),
        'employee': (
            'core.EmployeeSerializer',
            {'source': 'employee', 'fields': ['id', 'url', 'name']}
        ),
        'branch': (
            'core.BranchSerializer',
            {'source': 'branch', 'fields': ['id', 'url', 'name']}
        )
    }


class SaleItemSerializer(SerializerBase):
    class Meta:
        model = models.SaleItem
        fields = '__all__'

    expandable_fields = {
        'sale': (
            'core.SaleSerializer',
            {'source': 'sale', 'fields': ['id', 'url']}
        ),
        'product': (
            'core.ProductSerializer',
            {'source': 'product', 'fields': ['id', 'url', 'name']}
        ),
        'branch': (
            'core.BranchSerializer',
            {'source': 'branch', 'fields': ['id', 'url', 'name']}
        )
    }
