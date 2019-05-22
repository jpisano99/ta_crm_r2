from my_app import db
import xlrd
from my_app.models import Bookings
from my_app.func_lib.open_wb import open_wb
from my_app.func_lib.add_hash_to_xls import add_hash_to_xls
from my_app.func_lib.push_list_to_xls import push_list_to_xls
import datetime
from datetime import datetime as dt

#
# db.create_all()
#

Bookings.__table__.drop(db.session.bind)
Bookings.__table__.create(db.session.bind)

# For adjusting the date added as needed
now = dt.now()
now = now + datetime.timedelta(days=-40)

# Add a hash to this sheet
xlrd_wb, xlrd_ws = open_wb('tmp_TA Master Bookings.xlsx')
a_sheet = add_hash_to_xls(xlrd_wb, xlrd_ws, now)
push_list_to_xls(a_sheet, 'tmp_TA Master Bookings_hashed.xlsx')


# Now open the sheet that includes a unique hash value
xlrd_wb, xlrd_ws = open_wb('tmp_TA Master Bookings_hashed.xlsx')

# Loop over the sheet starting row 1 to exclude headers
for row_num in range(1, xlrd_ws.nrows):
    a_booking = Bookings()

    a_booking.erp_end_customer_name = xlrd_ws.cell_value(row_num, 0)
    a_booking.total_bookings = xlrd_ws.cell_value(row_num, 1)
    a_booking.product_id = xlrd_ws.cell_value(row_num, 17)

    date_cell = xlrd_ws.cell(row_num, 18)
    a_booking.date_added = datetime.datetime(*xlrd.xldate_as_tuple
                                            (date_cell.value, xlrd_wb.datemode))

    a_booking.hash_value = xlrd_ws.cell_value(row_num, 19)
    db.session.add(a_booking)

db.session.commit()
exit()

