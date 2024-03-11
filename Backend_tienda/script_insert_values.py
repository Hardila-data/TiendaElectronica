import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    c = connection.cursor()
    
    #Create the table
    query_create_table = """
        INSERT INTO TIENDA (name) VALUES('tienda Electronica');
    """

    c.execute(query_create_table)
    connection.commit()


        #Create the table
    query_create_table = """
        INSERT INTO usuario (name) VALUES('Pedro');
    """

    c.execute(query_create_table)
    connection.commit()
 

    #Create the table
    query_create_table = """
        INSERT INTO producto (sku,nombre,description,unidades_disponibles,
                                precio_unitario) VALUES('EA','RPI3','Boards Raspberry',285,164.934); """
    c.execute(query_create_table)
    connection.commit()
    #Create the table
    query_create_table = """
        INSERT INTO producto (sku,nombre,description,unidades_disponibles,
                                precio_unitario) VALUES('EA','ABX00003','Arduino Zero',25,243.950 ); """
    c.execute(query_create_table)
    connection.commit()
    
    query_create_table = """
        INSERT INTO producto (sku,nombre,description,unidades_disponibles,
                                precio_unitario) VALUES('WE','PS-55','Pasta para soldar 55gr ',20,14.994); """
    c.execute(query_create_table)
    connection.commit()
    
    query_create_table = """
        INSERT INTO producto (sku,nombre,description,unidades_disponibles,
                                precio_unitario) VALUES('SP','Desktop Kit 2G','Kit de escritorio Pi',4,550.018); """
    c.execute(query_create_table)
    connection.commit()


    c.close()

