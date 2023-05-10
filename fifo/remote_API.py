# we can access data from exernal APIs using the requests library
import requests

def makeCall():
    '''retrieve JSON data from a remote API'''
    apiURL = 'https://jsonplaceholder.typicode.com/todos'
    try:
        response = requests.get(apiURL) # make a call to the API
        # if the end-point ofers text, xml, html etc. then just read that
        response_l = response.json() # NB we dont need the JSON library, this is built in the requests
        print(type(response_l)) # NB the JSON is automatically converted to a structure (eg a List)
        # iterate over the returned data
        for item in response_l: # only works if we have an iterable
            print(f'Todo title {item["title"]} completed {item["completed"]}')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    makeCall()