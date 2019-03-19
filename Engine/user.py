#####################################
# Author : Mohd Shibli              #
# Description :                     #
#                                   #
# The following code will generate  #
# a private key for a particular    #
# user.                             #
#####################################


from Crypto.Hash import SHA256
import time
import sys
import binascii

class User:
    def __init__(self, user_details):
        self.user_details = user_details
        self.hash = SHA256.new()

    @property
    def generate_key(self):
        _name = self.user_details["name"];
        _nonce = str(int(time.time()))
        _token_value = _name + _nonce
        self.hash.update(_token_value.encode('utf-8'))
        return binascii.hexlify(self.hash.digest()).decode('utf-8')

if __name__ == '__main__':
    details = {
        "name" : "Shibli",
        "email" : "mohdshibli27@gmail.com"
    }

    user = User(details)
    sys.stdout.write(user.generate_key+"\n")
