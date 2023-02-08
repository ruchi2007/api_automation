import requests
from requests_oauthlib import OAuth1

url = "http://localhost:8888/uat_iqrashoppingdemo/wp-json/wc/v3/customers"
auth = OAuth1("ck_5f5597f5b2d75bbcc1023d7aeabe2cf44cac4ffa", "cs_27257f2341354ef1e410c8e4b6a2d8c800d49b83")
res = requests.get(url, auth=auth)
print(res.json())
assert res.status_code == 200, "invalid status code"
print(res.status_code)

content_type = res.headers["Content-type"]
assert content_type == "application/json; charset=UTF-8", "invalid content type"
print(content_type)
customer_list = res.json()
assert customer_list != [],"no existing customer"

print(res.json()[0]['id'])
print(res.json()[0]['first_name'])
print(res.json()[1]['last_name'])
print(res.json()[2]['username'])
print(res.json()[1]['email'])

for a in res.json():
    # print(a["id"])
    # print(a['first_name'])
    print(a['username'])
