import requests
from requests_oauthlib import OAuth1


url = "http://localhost:8888/uat_iqrashoppingdemo/wp-json/wc/v3/customers/5"
auth = OAuth1("ck_5f5597f5b2d75bbcc1023d7aeabe2cf44cac4ffa", "cs_27257f2341354ef1e410c8e4b6a2d8c800d49b83")
update_data = {
    "first_name": "atiqa",
    "last_name": "tahmid"}


res = requests.put(url, auth=auth, json=update_data)
print(res.status_code)
assert res.status_code == 200, "invalid status code"
assert res.status_code!= 201, "invalid status code"
print(res.status_code)
