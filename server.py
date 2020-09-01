from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import string
import hashlib


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()


# Generate random number
def genRandnumber(size=6, chars=string.ascii_uppercase + string.digits):

	return ''.join(random.choice(chars) for _ in range(size))
server.register_function(genRandnumber)

users = {"omar" : "pass123", "jan" : "pass456" }
rand = genRandnumber()


# method hasher() erstellt hashWert:
def hasher(random, password):
    key = random + password
    hashValue = hashlib.sha256(key.encode('utf-8'))
    return hashValue.hexdigest()


# Methode CompareHashes(user, hashValue) vergleicht Hashswerte von Cleint und Server
# sowie authentifiziert der User:
def compareHashes(user, hashValue):
    for user in users:
        if hasher(random, password) == hashValue:
            return "success"
        else:
            return "failed"
server.register_function(compareHashes)





'''
def hasher(password):
    if password == 'Pass123':
        key = hashlib.sha256(genRandnumber().encode('utf-8'))
        password + key.hexdigest()
        return "you're logged int!"

    elif password != 'Pass123':
        return "logging failed!", server.server_close()



server.register_function(hasher)

'''

# test function
def add(x, y):
    return x + y
server.register_function(add, 'add')



# Run the server's main loop
server.serve_forever()
