from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import hashlib
with open("C:\\Users\\cesgo\\desktop\\GitHub\\Cryptography\\Práctica 2\\Plaintext.txt",'r') as original_file:
        hash = original_file.read()
words=hash.split()
Hexhash=words[-1]
print(Hexhash)
words = words[:-1]
finaltext=' '.join(words)
print(finaltext)
result = hashlib.sha1(finaltext.encode())
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
if(result.hexdigest()==Hexhash):
    print("Son iguales")
else:
    print("Son diferentes")