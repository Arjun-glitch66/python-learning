#py -m pip install requests, put in terminal 

import requests

response=requests.get("https://example.com")
print(response.status_code)

#200 http response