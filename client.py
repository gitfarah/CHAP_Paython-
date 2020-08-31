import hashlib
import xmlrpc.client


s = xmlrpc.client.ServerProxy('http://localhost:8000')

users = {"omar" : "pass123", "jan" : "pass456" }



# method logger() logs users ein:
def logger():
    user = input("enter user: ")
    password = input("enter pass: ")

    # check!
    if user in users and password == users[user]:
        rand = s.genRandnumber()
        hashValue = hasher(rand, password)
        print(hashValue)
    else:
        return "failed"


# method hasher() erstellt hashWert:
def hasher(random, password):
    key = random + password
    hashValue = hashlib.sha256(key.encode('utf-8'))
    return hashValue.hexdigest()


logger()


