from model.user import User
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2 # колличество пользователей
f = "data/users.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif 0 == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(prefix, maxlen):
    symbols = string.digits
    return prefix.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


test_data = [
    User(first_name=random_string("firstname", 10), last_name=random_string("lastname", 10), address=random_string("address", 30),
         tel_home=random_number("home", 20), tel_mobile=random_number("mobile", 20), tel_work=random_number("work", 20),
         email=random_string("email", 20), email_2=random_string("email2", 20), email_3=random_string("email3", 20))
    for i in range(n)
]

# Путь
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out_f:
    jsonpickle.set_encoder_options("json", indent=2)
    out_f.write(jsonpickle.encode(test_data))
