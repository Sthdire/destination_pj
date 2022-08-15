import psycopg2
from psycopg2 import OperationalError, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def create_database(name_Database, password):
    connect = psycopg2.connect(dbname='postgres',
                               user='postgres',
                               host='localhost',
                               password=password)

    connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connect.cursor()
    try:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(name_Database)))
        print('successfully created database')
    except:
        print('Database already exists')
    pass


create_database('union', 'lololo2000')

con = psycopg2.connect(
    database='union',
    user="postgres",
    password='lololo2000',
    host="localhost",
    port="5432"
)
cur = con.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS doc_iform (
  number_ INTEGER,
  order_number INTEGER,
  usd_cost INTEGER,
  rub_cost INTEGER,
  delivery_time text
)
"""


def create_table(connection, table):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(table)
        print("Table executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    pass


create_table(con, create_users_table)

user_id_table = """
    CREATE TABLE IF NOT EXISTS user_id (
    user_id INTEGER,
    some_text text
    )
    """

create_table(con, user_id_table)

def save_values(number, order_number, usd_cost, delivery_time, rub_cost):
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO doc_iform (number_,order_number,usd_cost,rub_cost,delivery_time)
        VALUES (%s, %s, %s, %s, %s);
        """, (number, order_number, usd_cost, rub_cost, str(delivery_time)))
    con.commit()
    pass


def delete_values():
    cursor = con.cursor()
    cursor.execute('truncate table doc_iform')
    print("successfully delete values")
    pass


def get_values():
    cursor = con.cursor()
    cursor.execute("SELECT number_, order_number, usd_cost, rub_cost, delivery_time FROM doc_iform;")
    rows = cursor.fetchall()
    print("successfully got values")
    return rows


def set_user_id(user_id):
    cursor = con.cursor()
    cursor.execute("""
            INSERT INTO user_id (user_id, some_text)
            VALUES (%s, %s);
            """, (user_id, ''))
    con.commit()
    print('user id successfully saved')
    pass


def get_user_id():
    cursor = con.cursor()
    cursor.execute("SELECT user_id FROM user_id;")
    rows = cursor.fetchall()
    print("successfully got values")
    return rows
