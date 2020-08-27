
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import string
import hashlib
#from CLIENT import clientHash

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Generate random number
def genRandnumber(size=6, chars=string.ascii_uppercase + string.digits):

	return ''.join(random.choice(chars) for _ in range(size))
server.register_function(genRandnumber)

# Create server hash
password = 'Pass123'
key = hashlib.sha256(genRandnumber().encode('utf-8'))

def serverHash():

    return password + key.hexdigest()

# Compare own hash with client hash
'''
def compareHashes():
    if serverHash() == clientHash():
        print('Hashes match')
    else:
        print('Hashes do not match')
'''

# Run the server's main loop
server.serve_forever()
