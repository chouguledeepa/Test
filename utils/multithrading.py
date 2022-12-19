# """
# 42 elements - 11.75 seconds with 3 processes (multi-processing)
# 42 elements - 7.3 seconds with 8 processes (multi-processing)
# """
#
# import time
#
#
# # generic decorator
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         # pre-processing
#         start = time.time()
#         result = func(*args, **kwargs)
#         # post-processing
#         print(f"[ INFO ] time to execute - {time.time() - start}")
#         return result
#
#     return wrapper
#
#
# def compute_intensive_work(range_):
#     result = [i ** 3 for i in range(range_)]
#     return result
#
#
# @timeit
# def main():
#     large_number_range = [2000000, 2000000, 2000000, 2000000, 2000000, 2000000]
#
#
#     import multiprocessing
#     pool_ = multiprocessing.Pool(8)
#     pool_.map(compute_intensive_work, large_number_range)
#
#
# if __name__ == "__main__":
#     main()
#     breakpoint()
"""
pip install pymysql
pip install cryptography
# if you want to create new user and want to grant to root permissions to him
CREATE USER adam@localhost IDENTIFIED BY 'qwerty@123';
GRANT ALL PRIVILEGES ON *.* TO adam WITH GRANT OPTION;
SHOW GRANTS FOR adam;
"""

import pymysql
from typing import List


# connection to database
connection = pymysql.connect(
    host='localhost',
    user='adam',
    password='qwerty@123',
    database='starwarsDB'
 )

cursor = connection.cursor()
sql = "select * from starwarsDB.species_sample;"
result = cursor.execute(sql)


def get_db_conn():
    # connection to database
    connection_ = pymysql.connect(
        host='localhost',
        user='adam',
        password='qwerty@123',
        database='starwarsDB'
    )
    return connection_


def insert_resource(
        table_name: str,
        primary_key_: str,
        primary_value: int,
        columns_: List,
        values: List
):
    """
    Args:
        table_name (str):
        primary_key_ (str):
        primary_value (int):
        columns_ (list):
        values (list):
    Returns:
        number of records inserted in DB table
    """

    column_names = ", ".join(columns_)
    value_fields = ", ".join(values)

    column_names.rstrip(", ")
    value_fields.rstrip(", ")

    value_fields = ""
    for value in values:
        if isinstance(value, str):
            value_fields = value_fields + '''"''' + value + '''"''' + ''', '''
        elif isinstance(value, int):
            value_fields = value_fields + str(value) + ''','''

    value_fields = value_fields.rstrip(""", """)

    result = None
    with get_db_conn() as conn:
        cursor = conn.cursor()
        sql_magic = f"""insert into starwarsDB.{table_name} ({primary_key_}, {column_names}) values ({primary_value}, {value_fields});"""
        result = cursor.execute(sql_magic)
        conn.commit()
    return result