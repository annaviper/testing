```commandline
from json import dumps
payload = dumps({})
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# GET
requests.get("https://www.google.com")

requests.request("POST", url, headers=headers, data=payload)
requests.post(url=BASE_URI, data=payload, headers=headers)

requests.update()

requests.delete(url, )

response.json()
response.text
response.headers
```
# JSON
- Python dict to JSON:   
-- `json.dump()` to write to a file  
-- `json.dumps()` write to a JSON string

- JSON to dict:  
-- `json.load` read from a file  
-- `json.loads` read from a string, i.e. loads(response.text)
```commandline

```

# XML
```commandline
from lxml import etree

response_xml = response.text
tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
result = tree.xpath("//path/somewhere") # .text
```
or
```commandline
etree.XPath("//data/somewhere")
```

# Validate schema
Cerberus library