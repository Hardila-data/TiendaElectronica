from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_api.classes_tables.productos import Producto
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})



@api_view(['GET','POST']) 
def get_products(request):
    print(Producto.get_all_items()[0].id)
    productos = [{'id':producto.id,'sku':producto.sku,
                  'nombre':producto.nombre,'description':producto.description,
                  'unidades_disponibles':producto.unidades_disponibles,'precio_unitario':producto.precio_unitario,
                  } for producto in Producto.get_all_items()]
                  

    return Response({"productos": productos})

@api_view(['GET','POST','PUT']) 
def get_products_by_id(request,id_producto): 
    
    if request.method == 'GET':
        productos = [{'id':producto.id,'sku':producto.sku, 'nombre':producto.nombre,'description':producto.description,
                  'unidades_disponibles':producto.unidades_disponibles,'precio_unitario':producto.precio_unitario,
                  } for producto in Producto.get_item_by_id(id_producto)]

    if request.method == 'PUT':
        # cantidad_comprada = request.query_params.get('cantidad')
        cantidad_comprada = int(request.data['cantidad'])
        print('cantida',cantidad_comprada)
        #Obtener cantidad disponible
        productos = [{'id':producto.id,'sku':producto.sku, 'nombre':producto.nombre,'description':producto.description,
                  'unidades_disponibles':producto.unidades_disponibles,'precio_unitario':producto.precio_unitario,
                  } for producto in Producto.get_item_by_id(id_producto)]
        print(productos)
        quantity_registered = productos[0]['unidades_disponibles']
        print(quantity_registered)
        new_quantity = 0
        if quantity_registered > cantidad_comprada:
            new_quantity = quantity_registered - cantidad_comprada
        
        productos[0]['precio_unitario'] = new_quantity
        #Create a dictionary to updte the value

        Producto.update_unidades(id=productos[0]['id'],new_value=new_quantity)
        
        






        #productos[0].update_unidades()

        
                  

    return Response({"productos": productos})