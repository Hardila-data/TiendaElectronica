import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    c = connection.cursor()

    # #Create the table
    # query_create_table = """
    #     CREATE TABLE IF NOT EXISTS tienda(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT 
    #  )
    # """

    # c.execute(query_create_table)
    # connection.commit()

    #Create the table
    query_create_table = """
        CREATE TABLE IF NOT EXISTS producto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sku VARCHAR(10),
        nombre TEXT,
        description TEXT,
        unidades_disponibles INTEGER,
        precio_unitario FLOAT

     )
    """

    c.execute(query_create_table)
    connection.commit()

    # #Create the table
    # query_create_table = """
    #     CREATE TABLE IF NOT EXISTS usuario(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     name TEXT 
    #  )
    # """

    # c.execute(query_create_table)
    # connection.commit()


    #Create the table
    # query_create_table = """
    #     CREATE TABLE IF NOT EXISTS compras(
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     usuario VARCHAR(100),
    #     id_producto INTEGER,
    #     producto VARCHAR(200),
    #     cantidad INTEGER,
    #     fecha  DATETIME
    #     )
    # """

    # c.execute(query_create_table)
    # connection.commit()



    # c.close()




    c.close()

