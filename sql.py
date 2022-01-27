import sqlite3
def connect_database(database_name=':memory:'):
    return sqlite3.connect(database_name)
def create_table(connection, table_name, rownames, types, extra_fields=[]):
    if not extra_fields:
        extra_fields=['']*len(rownames)
    RETURN,all_data='\n',zip(rownames, types, extra_fields)
    connection.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} 
    ({f',{RETURN}'.join([' '.join(data_line) for data_line in all_data])})''')
def insert_data(connection, table_name, values_list, error_display='!ERROR default', show_errors=True):
    try:
        connection.execute(f"INSERT INTO COMPANY \
        VALUES {tuple(values_list)}")
        #In[8]: f'{(1, 2)}'
        #Out[8]: '(1, 2)'
    except Exception as e:
        print(show_errors*(str(e) if error_display=='!ERROR default' else error_display))
        # True*"a string" = "a string", False*"anything" = ""
def insert_datas(connection, table_name, values_lists, error_display='!ERROR default', show_errors=True):
    for values_list in values_lists:
        insert_data(connection, table_name, values_list, error_display, show_errors)
def commit_changes(connection):
    connection.commit()
def select_data(connection, table_name, rownames=['*'], constraints='1', ordering='', asc_or_desc='ASC', limit='-1'):
    return [list(row)
            for row in connection.execute(f"SELECT "
                                          f"{' AND '.join(rownames)} "
                                          f"FROM {table_name} "
                                          f"WHERE {constraints} "
                                          f"{bool(ordering) * f'ORDER {ordering} {asc_or_desc} LIMIT {limit}'}")]


