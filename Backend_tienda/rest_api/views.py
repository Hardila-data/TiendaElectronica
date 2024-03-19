from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from abc import ABC, abstractmethod
from rest_api.classes_tables.productos import Producto
import json

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
        
        return Response({"productos":productos})

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
        content = {'Products Deleted'}

        return Response(content, status=status.HTTP_200_OK)


class Regla(ABC):
    

    @abstractmethod
    def implemetacion_regla(self):
        pass


class ReglaEA(Regla):

    def implemetacion_regla(self, val, quanity):
        precio  =  val*quanity
        return precio


class ReglaWE(Regla):

    def implemetacion_regla(self, val, quanity):
        precio  =  val*quanity*1000
        return precio


class ReglaPS(Regla):

    def implemetacion_regla(self, val, quanity):
        
        pairs_3 = quanity/3
        denominador = quanity%3

        if (pairs_3 <1):
            return val*quanity 
        
        if (pairs_3 >=1):

        
            if((pairs_3==1)  and (denominador==0)):
                return (val*quanity - val*quanity*0.2)

        
            if ((pairs_3==2) and (denominador==0)): 
                return (val*quanity - val*quanity*0.4)
        

        
            if ((pairs_3>2)): 
                return (val*quanity - val*quanity*0.5)

    
            if(denominador>0):     
                return (val*quanity - val*quanity*0.2)
        




@api_view(['POST'])
def calculate_price_item(request):
    
    reglas ={
        'EA': ReglaEA().implemetacion_regla,
        'WE': ReglaWE().implemetacion_regla,
        'PS': ReglaPS().implemetacion_regla }
    
    if request.method == 'POST':
        
        body_json = json.loads(request.body.decode('utf-8'))
        
        sku = body_json['sku']
        quantity = float(body_json['quantity'])
        precio_unitario = float(body_json['precio_unitario'])

        regla_to_implement = reglas[sku]
        precio = regla_to_implement(quantity, precio_unitario)


        return Response({'precio':precio})

    else:
        return Response({'error': 'Wrong Rest Method'})
