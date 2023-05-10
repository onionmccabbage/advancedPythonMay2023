import sqlite3

def custom_read_db():
    '''Ask which creature to show'''
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    invalid = True # a handy flag
    while invalid:
        which_creature = input('Which creature? ')
        if type(which_creature)==str and which_creature !='':
            invalid = False
    st = f'''
    SELECT creature, count, cost FROM zoo
    WHERE creature="{which_creature}"
    '''
    try:
        curs.execute(st)
        conn.commit()
        rows = curs.fetchall()
        conn.close()
    except Exception as err:
        print(err) 
    for animal in rows:
        print(f'We have {animal[1]} {animal[0]} costing {animal[2]}') 

if __name__ == '__main__':
    custom_read_db()