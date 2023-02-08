# from pprint import pprint
import pytest
import requests

from config import config as cf
from resource import testData as td

customer_id = []

@pytest.mark.smoke
def test_tc10_post_creat_customer():
    endpoint = "/wp-json/wc/v3/customers"
    res = requests.post(cf.url + endpoint, auth=cf.auth, json=td.creat_random_customer_data)
    print(res.json()['id'])
    customer_id.append(res.json()['id'])
    print("\n tc10...............successful")

@pytest.mark.smoke
def test_tc20_get_customer_id():
    list_to_string = ''.join(map(str, customer_id))
    endpoint = "/wp-json/wc/v3/customers/" + list_to_string
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    print(res.json())
    print(res.json()['id'])
    print("\n tc20...............successful")

@pytest.mark.smoke
def test_tc30_update_customer():
    list_to_string = ''.join(map(str, customer_id))
    endpoint = "/wp-json/wc/v3/customers/" + list_to_string
    res = requests.put(cf.url + endpoint, auth=cf.auth, json=td.update_data)
    print(res.json()['id'])
    print("\n tc30...............successful")

@pytest.mark.smoke
def test_tc40_delete_customer():
    list_to_string = ''.join(map(str, customer_id))
    endpoint = "/wp-json/wc/v3/customers/" + list_to_string + "?force=true"
    res = requests.delete(cf.url + endpoint, auth=cf.auth)
    print(res.status_code)
    assert res.status_code == 200
    print("\n tc40...............successful")

@pytest.mark.smoke
def test_tc50_get_customer_should_not_exist():
    list_to_string = ''.join(map(str, customer_id))
    endpoint = "/wp-json/wc/v3/customers/" + list_to_string
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    assert res.status_code == 404
    print(res.status_code)
    print("\n tc50...............successful")
