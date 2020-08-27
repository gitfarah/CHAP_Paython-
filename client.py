import xmlrpc.client
import hashlib



s = xmlrpc.client.ServerProxy('http://localhost:8000')
password = 'Pass123'
key = hashlib.sha256(s.genRandnumber().encode('utf-8'))

def clientHash():

    return password + key.hexdigest()


print(clientHash())




# failed operation:
'''
token = password + s.genRandnumber()
key = hashlib.blake2b()
key.update(b'token')
'''

