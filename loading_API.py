# if we have the requests library we can use it to load external data from an API
import requests # may need to 'pip install requests'

def getData():
    apiURL = 'https://jsonplaceholder.typicode.com/photos'
    response = requests.get(apiURL) # make a request to the URL
    response_j= response.json() # we just want the JSON part of the response
    return response_j

if __name__ == '__main__':
    result = getData()
    print(result)