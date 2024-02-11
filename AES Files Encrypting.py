import os
import PySimpleGUI as sg
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, mode='ECB'):
    """
    Encrypts a file using AES (Advanced Encryption Standard)
    :param key: encryption key - should be either 16, 24, or 32 bytes long
    :param in_filename: input file
    :param out_filename: output file (if not specified, in_filename will be used)
    :param mode: mode of operation - can be one of ('ECB', 'CBC', 'CFB', 'OFB')
    :return: None
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0] + '_e' + mode

    with open(in_filename, 'rb') as infile:
        if mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)
        elif mode == 'CBC':
            cipher = AES.new(key, AES.MODE_CBC)
        elif mode == 'CFB':
            cipher = AES.new(key, AES.MODE_CFB)
        elif mode == 'OFB':
            cipher = AES.new(key, AES.MODE_OFB)

        with open(out_filename, 'wb') as outfile:
            outfile.write(cipher.encrypt(infile.read()))


def decrypt_file(key, in_filename, out_filename=None, mode='ECB'):
    """
    Decrypts a file using AES (Advanced Encryption Standard)
    :param key: encryption key - should be either 16, 24, or 32 bytes long
    :param in_filename: input file
    :param out_filename: output file (if not specified, in_filename will be used)
    :param mode: mode of operation - can be one of ('ECB', 'CBC', 'CFB', 'OFB')
    :return: None
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0] + '_d' + mode

    with open(in_filename, 'rb') as infile:
        if mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)
        elif mode == 'CBC':
            cipher = AES.new(key, AES.MODE_CBC)
        elif mode == 'CFB':
            cipher = AES.new(key, AES.MODE_CFB)
        elif mode == 'OFB':
            cipher = AES.new(key, AES.MODE_OFB)

        with open(out_filename, 'wb') as outfile:
            outfile.write(cipher.decrypt(infile.read()))

def main():
    layout = [[sg.Text("Select operation: "), sg.Radio("Encrypt", "RADIO1", default=True), 
                sg.Radio("Decrypt", "RADIO1")],
                [sg.Text("Select mode of operation: "), sg.Radio("ECB", "RADIO2", default=True), 
                sg.Radio("CBC",                "RADIO2"), sg.Radio("CFB", "RADIO2"), sg.Radio("OFB", "RADIO2")],
                [sg.Text("Select input file: "), sg.Input(), sg.FileBrowse()],
                [sg.Text("Key (16 bytes): "), sg.InputText()],
                [sg.Text("Initialization Vector (16 bytes): "), sg.InputText()],
                [sg.Submit(), sg.Cancel()]]

    window = sg.Window("AES File Encryption/Decryption", layout)

    while True:
        event, values = window.Read()

        if event in (None, "Cancel"):
            break

        operation = "Encryption" if values[0] == "Encrypt" else "Decryption"
        mode = values[1]
        in_file = values[2]
        
        if type(values[3]) == str:            
            if len(values[3]) != 16:
                print("Error key should be 16 bytes long")
            
            key = values[3].encode()
        else:
            print("Error key should be a string")
        
        if type(values[4]) == str:            
            if len(values[4]) != 16:
                print("Error iv should be 16 bytes long")
            
            iv = values[4].encode()
        else:
            print("Error iv should be a string")


        if operation == "Encryption":
            encrypt_file(key, in_file, mode=mode)
        else:
            decrypt_file(key, in_file, mode=mode)

        sg.Popup("File has been successfully {}ed!".format(operation), title="Success")

    window.Close()

if __name__ == "__main__":
    main()

