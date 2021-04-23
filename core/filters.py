from django.db.models import QuerySet, Q
from django_filters import filterset
from core import models

LIKE = 'icontains'


class NumberInFilter(filterset.BaseInFilter, filterset.NumberFilter):
    pass


class StateFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    abbreviation = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.State
        fields = ['name', 'abbreviation']


class CityFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    state_name = filterset.CharFilter(field_name='state__name', lookup_expr=LIKE)

    class Meta:
        model = models.City
        fields = ['name', 'state_name']


class ZoneFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Zone
        fields = ['name']


class DistrictFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    city_name = filterset.CharFilter(field_name='city__name', lookup_expr=LIKE)
    zone_name = filterset.CharFilter(field_name='zone__name', lookup_expr=LIKE)

    class Meta:
        model = models.District
        fields = ['name', 'city_name', 'zone_name']


class BranchFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    district_name = filterset.CharFilter(field_name='district__name', lookup_expr=LIKE)

    class Meta:
        model = models.Branch
        fields = ['name', 'district_name']


class SupplierFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    legal_document = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Supplier
        fields = ['name', 'legal_document']


class ProductGroupFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.ProductGroup
        fields = ['name']


class ProductFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    product_group = filterset.CharFilter(field_name='product_group__name', lookup_expr=LIKE)
    supplier = filterset.CharFilter(field_name='supplier__name', lookup_expr=LIKE)
    product_or_group = filterset.CharFilter(method='filter_product_or_group')

    @staticmethod
    def filter_product_or_group(queryset: QuerySet, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(product_group__name__icontains=value))

    class Meta:
        model = models.Product
        fields = ['name', 'product_group', 'supplier', 'product_or_group']


class MaritalStatusFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.MaritalStatus
        fields = ['name']


class DepartmentFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)

    class Meta:
        model = models.Department
        fields = ['name']


class CustomerFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    gender = filterset.CharFilter(lookup_expr=LIKE)
    district = filterset.CharFilter(field_name='district__name', lookup_expr=LIKE)
    marital_status = filterset.CharFilter(field_name='marital_status__name', lookup_expr=LIKE)

    class Meta:
        model = models.Customer
        fields = ['name', 'gender', 'district', 'marital_status']


class EmployeeFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    gender = filterset.CharFilter(lookup_expr=LIKE)
    department = filterset.CharFilter(field_name='department__name', lookup_expr=LIKE)
    district = filterset.CharFilter(field_name='district__name', lookup_expr=LIKE)
    marital_status = filterset.CharFilter(field_name='marital_status__name', lookup_expr=LIKE)
    start_salary = filterset.NumberFilter(field_name='salary', lookup_expr='gte')
    end_salary = filterset.NumberFilter(field_name='salary', lookup_expr='lte')
    salary_in = NumberInFilter(field_name='salary', lookup_expr='in')

    class Meta:
        model = models.Employee
        fields = [
            'name', 'gender', 'department', 'district',
            'marital_status', 'start_salary', 'end_salary', 'salary_in'
        ]


class SaleFilter(filterset.FilterSet):
    customer = filterset.CharFilter(field_name='customer__name', lookup_expr=LIKE)
    employee = filterset.CharFilter(field_name='employee__name', lookup_expr=LIKE)
    branch = filterset.CharFilter(field_name='branch__name', lookup_expr=LIKE)

    class Meta:
        model = models.Sale
        fields = ['customer', 'employee', 'branch']


class SaleItemFilter(filterset.FilterSet):
    product = filterset.CharFilter(field_name='product__name', lookup_expr=LIKE)

    class Meta:
        model = models.SaleItem
        fields = ['product']
