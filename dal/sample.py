"""
pip install pymysql
pip install cryptography
# if you want to create new user and want to grant to root permissions to him
CREATE USER adam@localhost IDENTIFIED BY 'qwerty@123';
GRANT ALL PRIVILEGES ON *.* TO adam WITH GRANT OPTION;
SHOW GRANTS FOR adam;
"""

import pymysql


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
print(result)
