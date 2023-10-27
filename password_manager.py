from cryptography.fernet import Fernet
import sys
'''
def write_key():
    key = Fernet.generate_key()
    with open ("Key.key","wb") as key_file:
        key_file.write(key)'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

master_password = input("What is the master password?")
if master_password != "Sri":
    print("Invalid password")
    sys.exit()

def view():
    with open("Password.txt",'r') as file:
        for f in file.readlines():
            data = f.rstrip()
            username,password = data.split("|")
            print("Username:",username,"| Password:", Fernet.decrypt(password.encode()).decode())

def add():
    username = input("Enter username?")
    password = input("Enter password")
    with open("Password.txt",'a') as file:
        file.write(username +"|" + Fernet.encrypt(password.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view the existing ones(view or add)? or press q to quit").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue