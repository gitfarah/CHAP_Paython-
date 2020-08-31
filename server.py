from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import string
import hashlib
import sys


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

# Users Dic
users = {"omar" : "pass123", "jan" : "pass456" }

# Stroing generated random string in "rand"
rand = genRandnumber()


# method hasher() erstellt hashWert:
def hasher(random, password):
    key = random + password
    hashValue = hashlib.sha256(key.encode('utf-8'))
    return hashValue.hexdigest()


# test function
def add(x, y):
    return x + y
server.register_function(add, 'add')



# Run the server's main loop
server.serve_forever()