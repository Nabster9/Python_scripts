import base64
from urllib.parse import quote, unquote

'''
iv=Q6v0mkoolcY%3D 
auth=YmRtaW5pc3RyYXRvci0tymyHOdZwTSk%3D
'''

def main():
    decoded_iv=bytearray(base64.b64decode(unquote("Q6v0mkoolcY%3D")))
    decoded_auth=bytearray(base64.b64decode(unquote("YmRtaW5pc3RyYXRvci0tymyHOdZwTSk%3D")))

    #print(decoded_iv[0])
    decoded_iv[0] ^= ord(chr(ord('a')^ord('b')))
    print(bytes.fromhex(str(decoded_auth[0])))
    decoded_auth[0]= ord('a')

    new_iv = quote(base64.b64encode(decoded_iv))
    new_auth = quote(base64.b64encode(decoded_auth))

    print(new_iv)
    print(new_auth)

    
if __name__ == "__main__":
    main()
