import json
import requests

res = requests.get('https://jasonplaceholder.typicode.com/todos')

print(res.status_code)