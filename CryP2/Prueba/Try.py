from tkinter import *
from tkinter import filedialog
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import hashlib
from tkinter import messagebox
import os
import base64
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA1
encoded_encrypted_msg=" "
def export_private_key(private_key,filename):
    with open(filename,"wb") as file:
        file.write(private_key.exportKey('PEM'))
        file.close
def export_public_key(public_key1,filename):
    with open(filename,"wb") as file:
        file.write(public_key1.exportKey('PEM'))
        file.close
def Firmar():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    archivo=os.path.split(filename)
    with open(os.path.join(os.path.dirname(__file__),filename),'rb') as original_file_hash:
        originalhash = original_file_hash.read()
    privatekey = RSA.import_key(open(archivo[0]+"/private_key.pem", "rb").read())
    result = SHA1.new(originalhash)
    signature = pkcs1_15.new(privatekey).sign(result)
    print(signature)
    with open(os.path.join(os.path.dirname(__file__),filename),'a') as original_to_sign:
        encoded_encrypted_msg = base64.b64encode(signature)
        original_to_sign.write(" "+str(encoded_encrypted_msg))
        original_to_sign.close
    """result = hashlib.sha1(originalhash.encode())
    print(result.hexdigest())
    with open("Práctica 2/Digest.txt","wb") as file:
        file.write(result.digest()) #To binary
        file.close
    with open(os.path.join(os.path.dirname(__file__),archivo[0]+"/Digest.txt"),'rb') as original_file_rsa:
        originalrsa = original_file_rsa.read()
    privatekey = RSA.import_key(open(archivo[0]+"/private_key.pem", "rb").read())
    OAEP_cipher = PKCS1_OAEP.new(privatekey)
    encryptedMsg = OAEP_cipher.encrypt(originalrsa)
    print(encryptedMsg)
    with open(os.path.join(os.path.dirname(__file__),filename),'a') as original_to_sign:
        encoded_encrypted_msg = base64.b64encode(encryptedMsg)
        original_to_sign.write(" "+str(encoded_encrypted_msg))
        original_to_sign.close
    print(encoded_encrypted_msg)"""
def Corroborar():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    archivo=os.path.split(filename)
    with open(os.path.join(os.path.dirname(__file__),filename),'r') as original_file:
        hash = original_file.read()
        words=hash.split()
        signature=words[-1]
        words = words[:-1]
        finaltext=' '.join(words)
        original_file.close()
    with open(os.path.join(os.path.dirname(__file__),filename),'w') as original_file:
        original_file.write(finaltext)
    with open(os.path.join(os.path.dirname(__file__),filename),'rb') as original_file_hash:
        originalhash = original_file_hash.read()
    #arr2 = bytes(signature, 'ascii')
    #signature=words[2:-1] 
    #firma=base64.b64decode(signature)  
    #words=hash.split()
    #signature=words[-1]
    #Hexhashrsa=Hexhashrsa[2:-1]
    #print(Hexhashrsa)
    #words = words[:-1]
    #print(words)
    publickey = RSA.import_key(open(archivo[0]+"/public_key.pem", "rb").read())
    #decoded_encrypted_msg = base64.b64decode(finaltext)
    h = SHA1.new(originalhash)
    print(h.digest())
    print(h.hexdigest())
    print(signature)
    signature=signature[2:-1]
    signature=bytes(signature,'UTF-8')
    print(signature)
    encoded_encrypted_msg = base64.b64decode(signature)
    print(encoded_encrypted_msg)
    #OAEP_cipher = PKCS1_OAEP.new(publickey)
    #decoded_encrypted_msg = base64.b64decode(Hexhashrsa)
    #print(decoded_encrypted_msg)
    #verifier = PKCS1_v1_5.new(publickey)
    #h = hashlib.sha1(finaltext.encode())
    #decryptedMsg = OAEP_cipher.decrypt(decoded_encrypted_msg)
    #result = hashlib.sha1(finaltext.encode())
    try:
        pkcs1_15.new(publickey).verify(h,encoded_encrypted_msg)
        messagebox.showinfo(title="Succesfuly",message="El mensaje proviene de Alicia")
    except(ValueError,TypeError):
        messagebox.showinfo(title="Wrong",message="El mensaje no proviene de Alicia, ha sido intervenido")
def Llave():
    keypair=RSA.generate(2048)
    public_key=keypair.publickey()
    export_private_key(keypair,"Práctica 2/private_key.pem")
    export_public_key(public_key,"Práctica 2/public_key.pem")
    messagebox.showinfo(title="Llaves",message="Par de llaves generado")
window=Tk()
window.geometry("200x150+100+100")
window.title("Práctica 2")
btnftxt=Button(window,text="Firmar",font=("Courier New",12),width=20,height=2,command=Firmar).grid(row=0,column=0)
btnctxt=Button(window,text="Corroborar",font=("Courier New",12),width=20,height=2,command=Corroborar).grid(row=1,column=0)
btnkey=Button(window,text="Generar Llave",font=("Courier New",12),width=20,height=2,command=Llave).grid(row=2,column=0)
window.mainloop()