import sqlite3

class Producto:

    def __init__(self,id, sku,nombre,description, unidades_disponibles,precio_unitario ) -> None:
        
        self.id = id
        self.sku = sku
        self.nombre = nombre
        self.description = description
        self.unidades_disponibles = unidades_disponibles
        self.precio_unitario = precio_unitario
        

    @classmethod
    def get_all_items(cls):
        with sqlite3.connect("db.sqlite3") as connection:
            c = connection.cursor()
            # use a for loop to iterate through the database, printing the results line by
            productos_list = [Producto(id=row[0],sku=row[1], nombre=row[2]\
                       ,description=row[3],unidades_disponibles=row[4],\
                       precio_unitario=row[5]) for row in c.execute("SELECT * from producto;")]
                
            return productos_list

    @classmethod
    def get_item_by_id(cls, id_producto):
        with sqlite3.connect("db.sqlite3") as connection:
            c = connection.cursor()
            # use a for loop to iterate through the database, printing the results line by
            productos_list = [Producto(id=row[0],sku=row[1], nombre=row[2]\
                       ,description=row[3],unidades_disponibles=row[4],\
                       precio_unitario=row[5]) for row in c.execute(f"SELECT * from producto WHERE id={id_producto};")]
                
            return productos_list

    @classmethod
    def update_unidades(cls,id,new_value):
        with sqlite3.connect("db.sqlite3") as connection:
            c = connection.cursor()
            c.execute(f"""UPDATE producto SET
                      unidades_disponibles={new_value} WHERE id={id}; """)
            


         

