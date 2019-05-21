from my_app.models import *

def build_sales_list(hierarchy):

    # Build SQL Stmnt from the hierarchy list
    sql_where = ""
    sql_columns = ""
    for key,value in hierarchy.items():
        print ("Request: ",key," / ",value)

    # If the first level is none then we are just starting
    if hierarchy["level1"] == None:
        # Adjust SQL stmnt for a starter list
        level = 1
        sql_columns = "`Sales_Level_1` "
        sql_where = ""
    else:
        #loop through the dict keys in level order
        #stop if we hit a value of None
        for level in range(1,6):
            next_key = "level"+str(level)
            if level == 5 :
                break
            elif hierarchy[next_key] == None :
                break
            else:
                sql_col_name = "`Sales_Level_" + str(level) + "` "
                sql_where = sql_where + sql_col_name + "=" + " '" + hierarchy[next_key] + "' AND "
                sql_columns = sql_columns + "," + sql_col_name

        # Add one add'l column to the request
        sql_columns = sql_columns + "," + "`Sales_Level_" + str(level) + "` "

        # Trim these up
        sql_where = "WHERE " + sql_where.rstrip("AND ")
        sql_columns = sql_columns.lstrip(", ")

    # Build the SQL Statement
    sql = "SELECT DISTINCT " + \
            sql_columns + \
            "FROM sales_levels " + \
            sql_where  + \
            " order by `Sales_Level_1`"
    print("SQL:  ",sql)

    # # Run the Query
    query_results = db.engine.execute(sql)

    # Construct the response list
    level_list = []
    for x in query_results:
        level_list.append(x.values()[level-1])

    print("Response:   ",level_list)

    return (level_list)

if __name__ == "__main__":
    from application.models import *
    from application.my_functions import *
    test_it = {'level2': 'US COMMERCIAL', 'level1': "Americas", 'level4': None, 'level3': None}
    build_sales_list(test_it)
