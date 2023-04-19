#Modificar para ser adaptado para a situação do projeto
#Introduzir dados relevantes
#Compreender ao ler PL06 e ver versao resolvida


import sqlite3
from os.path import isfile
def connect_db(dbname):
    db_is_created = isfile(dbname) # Existe ficheiro da base de dados?
    connection = sqlite3.connect('proj3.db') #DF - criamos a DB onde?
    cursor = connection.cursor()
    if not db_is_created:
        cursor.execute("CREATE TABLE if NOT EXISTS legs (id INTEGER PRIMARY KEY,dep_IATA TEXT,arr_IATA TEXT,dep_datetime TEXT,arr_datetime TEXT,duration_min numeric(2),airline_codes TEXT,;")
        connection.commit()
    return connection, cursor
um_registo = ("xyzx","LIS","MAD",202304051201,202304051405,65,"TP UA")   #Mudar 
varios_registos=[("qrtx",'LIS','BER',"...","...","...")
("abcd","MAD","LIS","...","...","...")]   #ESTES valores para apropriados para o novo contexto
if __name__ == '__main__':
    conn, cursor = connect_db('proj3.db')
    cursor.execute('INSERT INTO legs VALUES (?, ?, ?, ?,?,?)', um_registo)
    conn.commit()
    cursor.executemany('INSERT INTO legs VALUES (?, ?, ?, ?,?,?)', varios_registos)
    conn.commit()
    cursor.execute('SELECT * FROM legs') # Fazer query e obter todos
    todos = cursor.fetchall() # os resultados
    print ("Todos: ", todos)
    cursor.execute('SELECT * FROM legs') # Fazer query e obter um a um
    registo = cursor.fetchone()
    while registo:
        print ("Mais um: ", registo)
        registo = cursor.fetchone()
        cursor.execute('SELECT * FROM legs') # Fazer query e obter em grupos
        registos = cursor.fetchmany(size = 2)
    while registos:
        print ("Grupo: ",registos)
        registos = cursor.fetchmany(size = 2)
        conn.close()