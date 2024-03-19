from django.urls import path

from rest_api import views

urlpatterns = [
    path('default', views.hello_world, name='hello_world'),
    path('productos', views.get_products, name='get_productos'),
    path('productos/<int:id_producto>', views.get_products_by_id, name='get_products_by_id'),
    path('calculate_price_item', views.calculate_price_item, name='calculate_price_item')
]
