import psycopg2
from psycopg2 import OperationalError

con = psycopg2.connect(
    database="union",
    user="postgres",
    password="lololo2000",
    host="localhost",
    port="5432"
)
cur = con.cursor()

create_users_table = """
CREATE TABLE IF NOT EXISTS doc_iform (
  id SERIAL PRIMARY KEY,
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
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


# create_table(con, create_users_table)


def save_values(number, order_number, usd_cost, rub_cost, delivery_time):
    cursor = con.cursor()
    cursor.execute("""
        INSERT INTO doc_iform (number_,order_number,usd_cost,rub_cost,delivery_time) 
        VALUES (%s, %s, %s, %s, %s);
        """, (number, order_number, usd_cost, rub_cost, str(delivery_time)))
    con.commit()
    print('successfully saved values')


def get_values():
    cursor = con.cursor()
    cursor.execute("SELECT number_, order_number, usd_cost, rub_cost, delivery_time FROM doc_iform;")
    rows = cursor.fetchall()
    print("successfully got values")
    return rows


def update_values(value_target, value, number__target):
    cursor = con.cursor()
    if value_target == 'order_number':
        cursor.execute("""UPDATE doc_iform SET order_number = %s WHERE number_ = %s""", (value, number__target))
    elif value_target == 'usd_cost':
        cursor.execute("""UPDATE doc_iform SET usd_cost = %s WHERE number_ = %s""", (value, number__target))
    elif value_target == 'rub_cost':
        cursor.execute("""UPDATE doc_iform SET rub_cost = %s WHERE number_ = %s""", (value, number__target))
    elif value_target == 'delivery_time':
        cursor.execute("""UPDATE doc_iform SET delivery_time = %s WHERE number_ = %s""", (value, number__target))
    elif value_target == 'number_':
        cursor.execute("""UPDATE doc_iform SET number_ = %s WHERE number_ = %s""", (value, number__target))
    else:
        print('incorrect value_target')
    print("successfully changed value")
