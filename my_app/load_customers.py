from my_app import db
from my_app.models import Customers, Services
from my_app.func_lib.open_wb import open_wb
from my_app.func_lib.add_hash_to_xls import add_hash_to_xls
from my_app.func_lib.push_list_to_xls import push_list_to_xls
import datetime

#
# db.create_all()
#

Customers.__table__.drop(db.session.bind)
Customers.__table__.create(db.session.bind)
# Services.__table__.drop(db.session.bind)
# Services.__table__.create(db.session.bind)

now = datetime.datetime.now()
print(now)


xlrd_wb, xlrd_ws = open_wb('tmp_TA Customer List.xlsx')
a_sheet = add_hash_to_xls(xlrd_wb, xlrd_ws)
push_list_to_xls(a_sheet, 'tmp_TA Customer List_hashed.xlsx')

xlrd_wb, xlrd_ws = open_wb('tmp_TA Customer List_hashed.xlsx')

print(xlrd_ws.nrows)
customer_list = []

for row_num in range(1, xlrd_ws.nrows):
    # print(wb.row_values(row_num, 1))
    # print(xlrd_ws.row_values(row_num, 0))

    a_cust = Customers()
    a_cust.customer_ultimate_name = xlrd_ws.cell_value(row_num, 0)
    a_cust.customer_erp_name = xlrd_ws.cell_value(row_num, 0)
    a_cust.date_added = now
    a_cust.hash_value = xlrd_ws.cell_value(row_num, 0)

    print(xlrd_ws.cell_value(row_num, 0))
    print(xlrd_ws.cell_value(row_num, 1))
    print(xlrd_ws.cell_value(row_num, 2))


    db.session.add(a_cust)
    # customer_list.append(xlrd_ws.row_values(row_num, 1))

db.session.commit()


print(customer_list)


exit()

#
# # my_cov = Coverage()
# my_cust = Customers()
#
#
# my_cust.first_name = 'Jim'
# my_cust.last_name = 'Pisano'
# #
# # my_cov.pss_name = 'Cash'
# # my_cov.tsa_name ='Jim'
# #
# #
# db.session.add(my_cust)
# # db.session.add(my_cov)
# #
# #
# db.session.commit()
#
# #print (my_cov)
#
