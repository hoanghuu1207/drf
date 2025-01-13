from django.urls import path

from . import views

urlpatterns = [
  path('', views.product_create_api_view), # /api/products/
  path('list/', views.product_list_create_api_view), # /api/products/list/
  path('<int:pk>/update/', views.product_update_api_view), # /api/products/<int:pk>
  path('<int:pk>/delete/', views.product_delete_api_view), # /api/products/<int:pk>
  path('<int:pk>/', views.product_detail_api_view), # /api/products/<int:pk>
]