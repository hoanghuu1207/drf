from rest_framework import serializers

from .models import Product

# serializers để chuyển đổi dữ liệu giữa các mô hình Django và định dạng JSON, XML hoặc cả hai

class ProductSerializer(serializers.ModelSerializer):
  my_discount = serializers.SerializerMethodField(read_only=True)
  class Meta:
    model = Product
    fields = [
      'id',
      'title',
      'content',
      'price',
      'sale_price',
      'my_discount',
    ]

  def get_my_discount(self, obj):
    if not hasattr(obj, 'id'):
      return None
    if not isinstance(obj, Product):
      return None
    return obj.get_discount()