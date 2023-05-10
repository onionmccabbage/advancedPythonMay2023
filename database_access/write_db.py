import sqlite3

def writeDB():
    '''Here we write one piece of data to our new database table'''
    conn = sqlite3.connect('my_db') # connect or create the db
    curs = conn.cursor()
    st   = '''
    INSERT INTO zoo
    VALUES ("Penguin", 16, 0.62)
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    writeDB()
