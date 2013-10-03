#!bin/python3
from hashlib import md5, sha256
f = open("./salt.txt")
salt = f.read()
f.close()
pw = input("Password to be hashed: ")
md5_plus_salt = md5(pw.encode('utf-8')).hexdigest() + salt
salted = sha256(md5_plus_salt.encode('utf-8')).hexdigest()
print(salted)