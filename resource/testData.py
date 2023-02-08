import random
import string
letters = string.digits
random = "".join(random.choice(letters)for i in range(3))

creat_random_customer_data = {
  "email": "bo.doee123"+random+"@example.com",
  "first_name": "John",
  "last_name": "Doee",
  "username": "bo.doee"+random,
  "password": "johne.doe"
}


update_data = {
  "first_name": "adil",
    "last_name": "tasmid"}
