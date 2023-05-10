import sqlite3

def readDB():
    '''Here we read one piece of data from our new database table'''
    conn = sqlite3.connect('my_db') # connect or create the db
    curs = conn.cursor()
    st   = '''
    SELECT creature, count, cost FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit()
        # now we can use the cursor to fetch data from the table
        rows = curs.fetchall()
        conn.close()
    except Exception as err:
        print(err)
    # we now have all the data from the table
    for animal in rows:
        print( f'we have {animal[1]} {animal[0]} each costing {animal[2]}' )

if __name__ == '__main__':
    readDB()
