import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
  # data = request.data or {} # Get data from request

  serializer = ProductSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    # instance = serializer.save()
    print(serializer.validated_data)
    return Response(serializer.data)
  return Response({"invalid": "not good data"}, status=400)
  '''
  instance = Product.objects.all().order_by('?').first()

  if instance:
    # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price']) # Convert model to dict, only include id and title fields
    data = ProductSerializer(instance).data
  return JsonResponse(data)
  # return JsonResponse(data) # Return application/JSON response
  # json_data = json.dumps(data)
  # return HttpResponse(json_data, headers={"content-type": "application/json"}) # Return text/html response
  '''