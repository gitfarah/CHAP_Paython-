import hashlib
import xmlrpc.client


s = xmlrpc.client.ServerProxy('http://localhost:8000', allow_none=True)

# user will be used globally in clientHasher() method
user = None

# clientHasher() method enables the user to login with password, username
# and once login is successful the method will call method genRandnumber()
# to generate random number and combine it with user password
# and then hash the combination. Eventually the hash will be send to server
def clientHasher():
    global user
    user = input("Username: ")
    passw = input("Password: ")
    f = open("users.txt", "r")
    for account in f.readlines():
        us, pw = account.strip().split("|")
        if (user == us):
            randomNum = s.genRandnumber()
            secret = passw + str(randomNum)
            hashValue = hashlib.sha256(secret.encode('utf-8'))
            return hashValue.hexdigest()
    return False




# user send hash value to server through calling compareHashes() method
# before calling the method user muss exist!
hash = clientHasher()
if(hash):
    print(s.compareHashes(hash,user))
else:
    print("user don't exist!")


# available method could be called and used as soon user is authenticated
print(s.add(4,4, user))