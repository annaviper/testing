import requests

url = 'http://www.google.com'
payload = {'field1': 1, 'field2': 'something'}

requests.get(url)
requests.get(url, auth=('username', 'password'))
requests.get(url, headers={'Authorization': 'Bearer token235872587'})

requests.post(url, json=payload)

requests.put(url, json=payload)

requests.delete(url)

