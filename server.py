from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import hashlib


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler) :
    rpc_paths = ('/RPC2',)


# Create server
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=RequestHandler, allow_none=True)
server.register_introspection_functions()

# i will write comments about these variables too:
omarIsLoggedIn = False
maxIsLoggedIn = False
jokerIsLoggedIn = False
randomNum = None


# getPasswordByUsername() method will return password based on available user
def getPasswordByUsername(username):
    f = open("users.txt", "r")
    for account in f.readlines():
        us, pw = account.strip().split("|")
        if (username in us):
            print("lol")
            return pw

# genRandnumber generates random number that will be stored afterwards:
def genRandnumber():
    global randomNum
    randomNum = random.randint(0,9999)
    return randomNum
server.register_function(genRandnumber)



# serverHasher generates hash from the server side:
def serverHasher(username) :
    password = getPasswordByUsername(username)
    secret = password + str(randomNum)
    hashValue = hashlib.sha256(secret.encode('utf-8'))
    return hashValue.hexdigest()
server.register_function(serverHasher)


# compareHashes checks if the returned hash from
# the server is equal to the hash from the client:
def compareHashes(hashValue,username):
    global omarIsLoggedIn
    global maxIsLoggedIn
    global jokerIsLoggedIn
    if serverHasher(username) == hashValue:
        if username == "omar" : omarIsLoggedIn = True
        elif username == "max" : maxIsLoggedIn = True
        elif username == "joker": jokerIsLoggedIn = True
        return 'login succeeded'
    else:
        return 'login failed'
server.register_function(compareHashes)


def userIsLoggedIn(username):
    print(username)
    if username == "omar": return omarIsLoggedIn
    elif username == "max": return maxIsLoggedIn
    elif username == "joker" : return jokerIsLoggedIn



# test function
def add(x, y, username) :
    print(x,y,username)
    print(userIsLoggedIn(username))
    if(userIsLoggedIn(username)):
        return x + y
    else:
        return "your not logged in!"


server.register_function(add, 'add')


# Run the server's main loop
server.serve_forever()
