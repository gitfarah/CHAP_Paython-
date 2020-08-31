
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

# Create server hasher
def hasher(password):
    if password == 'Pass123':
        key = hashlib.sha256(genRandnumber().encode('utf-8'))
        password + key.hexdigest()
        return "you're logged in!"

    elif password != 'Pass123':
        return "loggin failed!"
	sys.exit(0)
server.register_function(hasher)


# Notes to improve hasher 
'''
Users = {Omar, Max}

# Create clients()
def clients():
	login = input("Enter username: ")
	pass =  input("Enter password: ") 
	
	#check!
	if login in Users and pass == 
	


# Create serverHasher()
def serverHasher():
		password == 'Pass123':
		hash = password + genRandnumber()
		hashlib.sha256(hash.encode('utf-8'))
		return hash.hexdigest()
#server.register_function(hasher)

# Create clientHasher()
def clientHasher():
		password == 'Pass123':
		hash = password + genRandnumber()
		hashlib.sha256(hash.encode('utf-8'))
		return hash.hexdigest()
#server.register_function(serverHasher)
'''

# Notes for hashCompare
'''
def hashCompare():
    while (true):
	if serverHasher() == clientHasher():
		return "you're logged in"
		break
	elif serverHasher() != clientHasher():
		return "loggin failed, plz repeat"
	elif serverHasher() != clientHasher():
		return "loggin failed, plz repeat"
	elif serverHasher() != clientHasher():
		return "loggin failed, plz repeat"
	else:
		sys.exit(0)
		
'''


# test function
def add(x, y):
    return x + y
server.register_function(add, 'add')



# Run the server's main loop
server.serve_forever()
