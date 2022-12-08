import pymysql.cursors
from fixture.orm import ORMFixture

db = ORMFixture(host="10.10.12.212", name="addressbook", user="root", password="")

# try:
#     list_groups = db.get_group_list()
#     for item in list_groups:
#         print(item)
#     print(len(list_groups))
# finally:
#     pass

try:
    list_contacts = db.get_contact_list()
    for item in list_contacts:
        print(item)
    print(len(list_contacts))
finally:
    pass