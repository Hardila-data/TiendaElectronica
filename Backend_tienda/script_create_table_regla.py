import sqlite3

with sqlite3.connect('db.sqlite3') as connection:
    c = connection.cursor()

    #Create the table
    query_create_table = """
        CREATE TABLE IF NOT EXISTS regla(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        sku VARCHAR(40),
        regla TEXT,
        valor FLOAT
     )
    """

    c.execute(query_create_table)
    connection.commit()
    c.close()

