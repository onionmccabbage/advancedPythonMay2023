# JSON is a very common data format
import json # tools for working with JSON

def main():
    '''load a JSON file and explore the data'''
    try:
        fin= open('todos.json', 'rt') # read text
        all_j = fin.read()
        # convert to a list
        all_l = json.loads(all_j) # convert JSON text to a structure
        print(all_l)
        # we can make a list into JSON
        j = json.dumps(all_l)
        print(j)
        print(type(all_l), type(j))

    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()