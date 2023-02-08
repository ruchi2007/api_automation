import requests
from requests_oauthlib import OAuth1
import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))
url = "http://localhost:8888/uat_iqrashoppingdemo/wp-json/wc/v3/customers"
auth = OAuth1("ck_5f5597f5b2d75bbcc1023d7aeabe2cf44cac4ffa", "cs_27257f2341354ef1e410c8e4b6a2d8c800d49b83")
json_data = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doee",
  "username": "bo.doee"+random,
  "password": "johne.doe"
}
res = requests.post(url, auth=auth, data = json_data)
print(res.json())
assert res.status_code == 201, 'invalid status code'
assert res.status_code!= 200, "invalid status code"
print(res.status_code)

print(json_data["first_name"])
print(json_data["last_name"])
