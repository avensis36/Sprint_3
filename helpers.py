import random as r
import string
import re


def random_email():
    email = f'antonermolaev12{r.randint(100,999)}@gmail.com'
    return email

def random_password():
    alphabet = list(string.ascii_letters)
    password = ''
    while len(password) < 7:
        password += r.choice([alphabet[r.randint(0, 51)], str(r.randint(0, 9))])
    return password

def is_valid_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.match(pattern, email) is not None