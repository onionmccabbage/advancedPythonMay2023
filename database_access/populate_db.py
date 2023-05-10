import sqlite3

def populateDB():
    '''Here we write several pieces of data to our new database table'''
    creatures_t = ( # normally this comes from JSON or API etc.
        {'creature':'Albatros', 'count':1,      'cost':120.99},
        {'creature':'Bear',     'count':5,      'cost':323.56},
        {'creature':'Carp',     'count':120,    'cost':87.00},
        {'creature':'Deer',     'count':121,    'cost':12.99},
        {'creature':'Elk',      'count':7,      'cost':73.47},
    )    
    conn = sqlite3.connect('my_db') # connect or create the db
    curs = conn.cursor()
    # this statemetn has '?' as placeholders for actual values
    st   = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    # iterate over the creatures tuple
    for item in creatures_t:
        try:
            # validate we have suitable data
            if type(item['creature']==str):
                n = item['creature']
            else:
                raise Exception('Name mus be a string')
            if type(item['count']==int):
                c = item['count']
            else:
                raise Exception('Count must be a positive integer')
            if type(item['cost']==float):
                co = item['cost']
            else:
                raise Exception('Cost must be a positive float')
            # now use the sanitized data to inject each creatuere into the table
            curs.execute(st, (n, c, co)) # here we inject values to replace '?'
            conn.commit()
        except Exception as err:
            print(err)
    # after all the looping, tidy up
    conn.close()

if __name__ == '__main__':
    populateDB()