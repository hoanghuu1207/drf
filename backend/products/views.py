from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

  # perform_create cho phép bạn can thiệp vào quá trình tạo đối tượng mới, thêm logic tùy chỉnh hoặc xử lý dữ liệu trước khi lưu vào cơ sở dữ liệu
  def perform_create(self, serializer):
    # serializer.save(user=self.request.user)
    print(serializer.validated_data)
    title = serializer.validated_data.get("title")
    content = serializer.validated_data.get("content") or None
    if content is None:
      content = title
    serializer.save(content=content)

product_create_api_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_list_create_api_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  # lookup_field = 'id' # Default: 'pk'

product_detail_api_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(generics.UpdateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_update(self, serializer):
    instance = serializer.save()
    if not instance.content:
      instance.content = "instance.title"
      # instance.save()

product_update_api_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def perform_destroy(self, instance):
    super().perform_destroy(instance)

product_delete_api_view = ProductDeleteAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
  '''
  Not gonna use this. Use ProductListCreateAPIView instead(Just for GET request)
  '''
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

product_list_api_view = ProductListAPIView.as_view()


# not gonna using, use class view instead
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
  method = request.method

  if method == "GET":
    if pk is not None:
      # detail view
      obj = get_object_or_404(Product, pk=pk)
      data = ProductSerializer(obj, many=False).data
      return Response(data)
    else:
      # list view
      queryset = Product.objects.all()
      data = ProductSerializer(queryset, many=True).data
      return Response(data)
  if method == "POST":
    # create an item
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      title = serializer.validated_data.get("title")
      content = serializer.validated_data.get("content") or None
      if content is None:
        content = title
      serializer.save(content=content)
      return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)