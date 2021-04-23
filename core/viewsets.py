from rest_framework import viewsets
from core import models, serializers, mixins, filters


class ViewSetBase(viewsets.ModelViewSet, mixins.ViewSetExpandMixin):
    def list(self, request, *args, **kwargs):
        self.make_queryset_expandable(request)
        return super(ViewSetBase, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.make_queryset_expandable(request)
        return super(ViewSetBase, self).retrieve(request, *args, **kwargs)


class ZoneViewSet(viewsets.ModelViewSet):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer
    filter_class = filters.ZoneFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class StateViewSet(viewsets.ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer
    filter_class = filters.StateFilter
    ordering_fields = '__all__'
    ordering = ('id',)

class CityViewSet(ViewSetBase):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    filter_class = filters.CityFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class DistrictViewSet(viewsets.ModelViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    filter_class = filters.DistrictFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    filter_class = filters.SupplierFilter
    ordering_fields = '__all__'
    ordering = ('id',)

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer
    filter_class = filters.ProductGroupFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class BranchViewSet(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
    filter_class = filters.BranchFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filter_class = filters.DepartmentFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer
    filter_class = filters.MaritalStatusFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_class = filters.EmployeeFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    filter_class = filters.CustomerFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = models.Sale.objects.all()
    serializer_class = serializers.SaleSerializer
    filter_class = filters.SaleFilter
    ordering_fields = '__all__'
    ordering = ('id',)


class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = models.SaleItem.objects.all()
    serializer_class = serializers.SaleItemSerializer
    filter_class = filters.SaleItemFilter
    ordering_fields = '__all__'
    ordering = ('id',)
