import sqlite3

connection = sqlite3.connect('data.db')

def create_table(con):
    stmt = con.cursor()
    SQL = """
    CREATE TABLE IF NOT EXISTS "kunden" (
        "id"	INTEGER,
        "vorname"	TEXT,
        "nachname"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    );"""
    try:
        stmt.execute(SQL)
        con.commit() # Überträgt alle Anweisungen an die DB
    except sqlite3.OperationalError:
        print('Problem beim Erzeugen der Tabelle')

create_table(connection)

# CRUD 

def insert(con, vorname, nachname):
    stmt = con.cursor()
    SQL = 'INSERT INTO kunden VALUES(null, ?, ?)'
    stmt.execute(SQL, (vorname, nachname))
    con.commit()

insert(connection, 'Bruce', 'Banner')

def insert_all(con, liste):
    stmt = con.cursor()
    SQL = 'INSERT INTO kunden VALUES(null, ?, ?)'
    stmt.executemany(SQL, liste)
    con.commit()

#insert_all(connection, [('Natasha', 'Romanov'), ('Carol', 'Danvers'), ('Steve', 'Rogers')])

def read_all(con):
    stmt = con.cursor()
    stmt.execute('SELECT * FROM kunden')
    return stmt.fetchall()

#print(read_all(connection))

#for k in read_all(connection):
#    print(f"{k[0]} : {k[1]} {k[2]}")

def update_by_id(con, id, vorname, nachname):
    stmt = con.cursor()
    stmt.execute('UPDATE kunden SET vorname = ?, nachname = ? WHERE id = ?', (vorname, nachname, id))
    con.commit()

#update_by_id(connection, 5, 'Scott', 'Roberts')

def delete_by_id(con, id):
    stmt = con.cursor()
    stmt.execute('DELETE FROM kunden WHERE id = ?', (id,))
    con.commit()

#delete_by_id(connection, 1)
#delete_by_id(connection, 3)

#for k in read_all(connection):
#    print(f"{k[0]} : {k[1]} {k[2]}")

connection.close()