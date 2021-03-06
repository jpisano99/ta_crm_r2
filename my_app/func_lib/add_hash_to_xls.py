import hashlib
import xlrd
import datetime
from datetime import datetime as dt

from my_app.func_lib.open_wb import open_wb
from my_app.func_lib.push_list_to_xls import push_list_to_xls


def add_hash_to_xls(wb, ws, date_added=dt.now()):
    # This function takes in a xlrd workbook and xlrd worksheet
    # It adds a hash value to the last column to uniquely identify the row
    # The function returns a list of rows ready to be written to an xlsx file

    my_new_sheet = []
    hash_dict = {}

    # Append columns called Date Added and Row Hash to the Header Row
    my_new_row = ws.row_values(0)
    my_new_row.append('Date Added')
    my_new_row.append('Row Hash')
    date_added_col = len(my_new_row) - 2
    hash_col = len(my_new_row) - 1
    my_new_sheet.append(my_new_row)

    for row_num in range(1, ws.nrows):
        my_new_row = ws.row_values(row_num)
        my_xlrd_row = ws.row(row_num)
        my_new_row.append('')  # place for the Date Added
        my_new_row.append('')  # place for the Hash Val
        my_new_sheet.append(my_new_row)
        list_to_hash = []

        # Walk across this input row from xlrd
        for col_num, cell in enumerate(my_xlrd_row):
            if cell.ctype == xlrd.XL_CELL_NUMBER:
                # Got an the xlrd CELL FLOAT to a str type
                cell_as_str = str(cell.value)
                list_to_hash.append(cell_as_str)
                new_cell_value = cell.value

            elif cell.ctype == xlrd.XL_CELL_DATE:
                # Convert the xlrd CELL DATE to a datetime type
                cell_as_date = datetime.datetime(*xlrd.xldate_as_tuple(cell.value, wb.datemode))
                cell_as_str = cell_as_date.strftime("%m/%d/%Y")
                list_to_hash.append(cell_as_str)
                new_cell_value = cell_as_date

            else:
                # Nothing to Convert here
                list_to_hash.append(cell.value)
                new_cell_value = cell.value

            # Add the new cell to the new row
            my_new_row[col_num] = new_cell_value

        # This will make list_to_hash type to all one big string called my_string
        str_to_hash = ''.join(list_to_hash)

        # Create a 32 character hash value and place it in the Hash Column
        hash_result = (hashlib.md5(str_to_hash.encode('utf-8')).hexdigest())

        tie_breaker = 1
        if hash_result in hash_dict:
            tie_breaker = hash_dict[hash_result] + 1
            hash_dict[hash_result] = tie_breaker
        else:
            hash_dict[hash_result] = tie_breaker

        my_new_row[date_added_col] = date_added
        my_new_row[hash_col] = hash_result + '-' + str(tie_breaker)

    return my_new_sheet


if __name__ == "__main__" and __package__ is None:
    xlrd_wb, xlrd_ws = open_wb('tmp_TA Master Bookings.xlsx')
    # wb, ws = open_wb('tmp_Master Renewals.xlsx')
    # xlrd_wb, xlrd_ws = open_wb('tmp_TA Customer List.xlsx')

    a_sheet = add_hash_to_xls(xlrd_wb, xlrd_ws)
    push_list_to_xls(a_sheet, 'tmp_TA Master Bookings_hashed.xlsx')
