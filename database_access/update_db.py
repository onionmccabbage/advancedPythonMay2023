import sqlite3

def custom_update_db():
    ''' ask for name and count, then update one data member'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    invalid = True # a handy flag
    while invalid:
        which_creature = input('Which creature needs updating? ')
        if type(which_creature)==str and which_creature !='':
            invalid = False
    qty = int(float(input('what is the updated quantity? ')))
    st = f'''
    UPDATE zoo
    SET count={qty}
    WHERE creature="{which_creature}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    custom_update_db()