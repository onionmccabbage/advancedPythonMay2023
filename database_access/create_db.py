import sqlite3 # this database is included with Python

# we need to make a connection to our db
def accessDB():
    '''This function will acces the sqlite3 database to create a table called Zoo
       This will include creature name (index), quantity and cost'''
    conn = sqlite3.connect('my_db') # connect or create the db
    # next we need a cursor to interact with the db
    curs = conn.cursor() # the cursor lets us execute SQL statements
    # first we will make a table for our data
    st = '''
    CREATE TABLE zoo
    (
        creature VARCHAR(32) PRIMARY KEY,
        count INT,
        cost FLOAT
    )
    '''
    try:
        curs.execute(st) # at this point the SQL is sent to the DB
        conn.commit()    # ...we commit the changes
        conn.close()     # ...and tidy up
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()