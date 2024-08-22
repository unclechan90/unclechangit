import requests as req
import pandas as pd

headers = {'Content-type': 'appliction/json', 'Accept': 'application/vnd.samanage.v2.1+json', 'X-Samanage-Authorization': 
           'Bearer UHJhZGlwYXQuY0BzYWxlcy50aGFpYmV2LmNvbQ==:eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjo1MTY2ODM2LCJnZW5lcmF0ZWRfYXQiOiIyMDI0LTA4LTAyIDEzOjQ5OjM5In0.yW7W1RO5tBq1-AAVL-LzOl-EVm7FOfVWW3Ctwq0PMWKoNW_vcQPsUjb8oGpWLxBKSxDmEP7PRYT9luXdKYYqKA:VVM='}
url = 'https://api.samanage.com/other_assets.json'
#payload = {'page':2 , 'count': 25}
#endpoint = 'character'
res = req.get(url, headers=headers) # params=payload)
data = res.json()
pages = data['info']['page']
print(pages)