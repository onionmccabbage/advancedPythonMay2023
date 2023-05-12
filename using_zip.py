# zip in Python has nothing to do with archives, zip-files etc.
# Long before that kind of zip, Python used zip to combine data

def main():
    '''We can use zip to combine separate data structures'''
    days_l   = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    fruits_t = ('Banana', 'Orange', 'Kiwi')
    drinks_s = {'Coffee', 'Tea', 'Water'}
    desserts = ['Tiramisu', 'Crumble', 'Crepe']

    # zip will use the minimum length collection for its output
    for day, fruit, drink, dessert in zip(days_l, fruits_t, drinks_s, desserts):
        print(f'On {day} I eat {fruit} with {drink} then {dessert}')

if __name__ == '__main__':
    main()