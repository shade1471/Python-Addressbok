import pymysql.cursors

connection = pymysql.connect(host="10.10.12.212", database="addressbook", user="root", password="")
# connection = mysql.connector.connect(host="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    # fetchall возвращает всю информацию что извлечена
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
