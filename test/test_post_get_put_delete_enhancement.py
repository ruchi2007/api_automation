# from pprint import pprint
import pytest
import requests
from config import config as cf
from resource import testData as td
import pytest


@pytest.mark.smoke
def test_tc1_post_creat_customer():
    global customer_id
    endpoint = "/wp-json/wc/v3/customers"
    res = requests.post(cf.url + endpoint, auth=cf.auth, json=td.creat_random_customer_data)
    customer_id = str(res.json()['id'])
    print(res.json()['id'])
    print(type(customer_id))
    print("\n tc1...............successful")


@pytest.mark.smoke
def test_tc2_get_customer_id():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    print(res.json())
    print(res.json()['id'])
    print("\n tc2...............successful")


@pytest.mark.smoke
def test_tc3_update_customer():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.put(cf.url + endpoint, auth=cf.auth, json=td.update_data)
    print(res.json()['id'])
    print("\n tc3...............successful")


@pytest.mark.smoke
def test_tc4_delete_customer():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id + "?force=true"
    res = requests.delete(cf.url + endpoint, auth=cf.auth)
    print(res.json()['id'])
    print(res.status_code)
    assert res.status_code == 200
    print("\n tc4...............successful")


@pytest.mark.smoke
def test_tc5_get_customer_should_not_exist():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    assert res.status_code == 404
    print(res.status_code)
    print("\n tc5...............successful")


# regression test

@pytest.mark.regression
def test_tc11_post_creat_customer():
    global customer_id
    endpoint = "/wp-json/wc/v3/customers"
    res = requests.post(cf.url + endpoint, auth=cf.auth, json=td.creat_random_customer_data)
    customer_id = str(res.json()['id'])
    print(res.json()['id'])
    print(type(customer_id))
    print("\n tc11...............successful")


@pytest.mark.regression
def test_tc21_get_customer_id():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    print(res.json())
    print(res.json()['id'])
    print("\n tc21...............successful")


@pytest.mark.regression
def test_tc31_update_customer():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.put(cf.url + endpoint, auth=cf.auth, json=td.update_data)
    print(res.json()['id'])
    print("\n tc31...............successful")


@pytest.mark.regression
def test_tc41_delete_customer():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id + "?force=true"
    res = requests.delete(cf.url + endpoint, auth=cf.auth)
    print(res.json()['id'])
    print(res.status_code)
    assert res.status_code == 200
    print("\n tc41...............successful")


@pytest.mark.regression
def test_tc51_get_customer_should_not_exist():
    endpoint = "/wp-json/wc/v3/customers/" + customer_id
    res = requests.get(cf.url + endpoint, auth=cf.auth)
    assert res.status_code == 404
    print(res.status_code)
    print("\n tc51...............successful")
