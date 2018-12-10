import hashlib
import random
from django.contrib.auth import hashers

from django.test import TestCase
email = 'test@test.com'
salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
activation_key = hashlib.sha1((email + salt).encode('utf8')).hexdigest()
print(activation_key)