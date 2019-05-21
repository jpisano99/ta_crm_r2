from my_app import db
from my_app.models import Customers, Services
from my_app.func_lib.open_wb import open_wb
import datetime

#
# db.create_all()
#

# Customers.__table__.drop(db.session.bind)
# Customers.__table__.create(db.session.bind)
Services.__table__.drop(db.session.bind)
Services.__table__.create(db.session.bind)

now = datetime.datetime.now()
print(now)


# ws, wb = open_wb('tmp_TA Customer List.xlsx')
ws, wb = open_wb('tmp_TA AS SKUs.xlsx')
print(wb.nrows)
customer_list = []

for row_num in range(wb.nrows):
    # print(wb.row_values(row_num, 1))
    print(wb.row_values(row_num, 0)[0])
    a_cust = Services()
    a_cust.customer_name = wb.row_values(row_num, 0)[0]
    a_cust.as_sku= wb.row_values(row_num, 0)[1]
    a_cust.date_added = now
    db.session.add(a_cust)
    customer_list.append(wb.row_values(row_num, 1))

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
