# Frontend app
import requests
import json
import numpy as np

from fignerprint import fingerprint
from encrypt import *

fingerprint_vector = fingerprint()

empty_str = ''
for i in fingerprint_vector:
    empty_str = empty_str + str(int(i))

fingerprint_vector = int(empty_str)

keyPairClient = generateKeyPair()

ciphertext = encrypt(keyPairClient["publicKey"], fingerprint_vector)

print(len(hex(ciphertext['C2'])))

# The URL of the backend app
url = "http://localhost:5000/post"

# The data to send as a post request
data = {"username": "Alice", "fingerprint": hex(ciphertext['C2'])}

# Convert the data to JSON format
data_json = json.dumps(data)

# The headers to specify the Content-Type
headers = {"Content-Type": "application/json"}

# Send the post request and get the response
response = requests.post(url, data=data_json, headers=headers)

# Print the status code and the content of the response
print(response.status_code)
print(response.content)