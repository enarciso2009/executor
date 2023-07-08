import sqlite3
database = "banco.db"
import sqlite3 as sql


# select nas tabelas

def select_horainicio():
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"select * from cad_inicio")
    rows = trans.fetchall()
    trans.disconnect()
    print(rows)
    return rows

def select_horatermino():
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"select * from cad_termino")
    rows = trans.fetchall()
    trans.disconnect()
    print(rows)
    return rows

def select_servico():
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"select exec from cad_executor")
    rows = trans.fetchall()
    trans.disconnect()
    print(rows)
    return rows

def select_status():
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"select status from cad_status")
    rows = trans.fetchall()
    trans.disconnect()
    print(rows)
    return rows

#insere nas tabelas

def insert_cad_inicio(hora1, hora2, hora3, hora4, hora5, hora6, hora7, hora8, hora9, hora10, hora11, hora12):
    print('entrou no insert em banco')
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"INSERT INTO CAD_INICIO VALUES('{hora1}','{hora2}', '{hora3}', '{hora4}', '{hora5}','{hora6}', '{hora7}', '{hora8}', '{hora9}', '{hora10}', '{hora11}','{hora12}')")
    trans.persist()
    trans.disconnect()

def insert_cad_termino(hora13, hora14, hora15, hora16, hora17, hora18, hora19, hora20, hora21, hora22, hora23, hora24):
    print('entrou no insert em banco')
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"INSERT INTO CAD_TERMINO VALUES('{hora13}','{hora14}', '{hora15}', '{hora16}', '{hora17}','{hora18}', '{hora19}', '{hora20}', '{hora21}', '{hora22}', '{hora23}','{hora24}')")
    trans.persist()
    trans.disconnect()

def insert_cad_executor(exec):
    print('entrou no insert em banco')
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"INSERT INTO CAD_EXECUTOR VALUES('{exec}')")
    trans.persist()
    trans.disconnect()

def insert_cad_status(numero):
    print('entrou no insert em banco')
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"INSERT INTO CAD_STATUS VALUES('{numero}')")
    trans.persist()
    trans.disconnect()

# update nas tabelas
def update_cad_status(numero):
    print('entrou no update em cad_status')
    trans = TransactionObject()
    trans.connect()
    trans.execute(f"UPDATE CAD_STATUS SET STATUS = {numero}")
    trans.persist()
    trans.disconnect()


#Conectando ao banco de dados
conn = sqlite3.connect(database)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS CAD_INICIO(HORA1 TEXT, HORA2 TEXT, HORA3 TEXT, HORA4 TEXT, HORA5 TEXT, HORA6 TEXT, HORA7 TEXT, HORA8 TEXT, HORA9 TEXT, HORA10 TEXT, HORA11 TEXT, HORA12 TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS CAD_TERMINO(HORA13 TEXT, HORA14 TEXT, HORA15 TEXT, HORA16 TEXT, HORA17 TEXT, HORA18 TEXT, HORA19 TEXT, HORA20 TEXT, HORA21 TEXT, HORA22 TEXT, HORA23 TEXT, HORA24 TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS CAD_EXECUTOR(EXEC TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS CAD_STATUS(STATUS)")
conn.commit()
conn.close()

class TransactionObject():
    database = 'banco.db'
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql):
        if TransactionObject.connected:
            if sql == None:
                print(f'chegou aqui sql: {sql}')
                TransactionObject.cur.execute(sql)
            else:
                print(f'chegou no else sql {sql}')
                TransactionObject.cur.execute(sql)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS CAD_INICIO(HORA1 TEXT, HORA2 TEXT, HORA3 TEXT, HORA4 TEXT, HORA5 TEXT, HORA6 TEXT, HORA7 TEXT, HORA8 TEXT, HORA9 TEXT, HORA10 TEXT, HORA11 TEXT, HORA12 TEXT)")
    trans.execute("CREATE TABLE IF NOT EXISTS CAD_TERMINO(HORA13 TEXT, HORA14 TEXT, HORA15 TEXT, HORA16 TEXT, HORA17 TEXT, HORA18 TEXT, HORA19 TEXT, HORA20 TEXT, HORA21 TEXT, HORA22 TEXT, HORA23 TEXT, HORA24 TEXT)")
    trans.execute("CREATE TABLE IF NOT EXISTS CAD_EXECUTOR(EXEC TEXT)")
    trans.execute("CREATE TABLE IF NOT EXISTS CAD_STATUS(STATUS)")
    trans.persist()
    trans.disconnect()
initDB()