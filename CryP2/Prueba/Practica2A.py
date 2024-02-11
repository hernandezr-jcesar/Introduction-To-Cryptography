from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import hashlib
with open("C:\\Users\\cesgo\\desktop\\GitHub\\Cryptography\\Práctica 2\\Plaintext.txt",'r') as original_file:
        originalhash = original_file.read()
result = hashlib.sha1(originalhash.encode())
with open("C:\\Users\\cesgo\\desktop\\GitHub\\Cryptography\\Práctica 2\\Plaintext.txt",'rb') as original_file:
        originalrsa = original_file.read()
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
privatekey = RSA.import_key(open("C:\\Users\\cesgo\\desktop\\GitHub\\Cryptography\\Práctica 2\\private_key.pem", "rb").read())
OAEP_cipher = PKCS1_OAEP.new(privatekey)
encryptedMsg = OAEP_cipher.encrypt(originalrsa)
"""with open("CipherText.txt","wb") as file:
        file.write(result.digest()) #To binary
        file.close"""
with open("C:\\Users\\cesgo\\desktop\\GitHub\\Cryptography\\Práctica 2\\Plaintext.txt",'a') as original_file:
        original_file.write(" "+result.hexdigest())
        original_file.close
