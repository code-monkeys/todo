#!bin/python3
from hashlib import md5, sha256
salt = "+TmLir8DYItc0QSYg3SRR4k7X76K+/VfHxjb0LAQq/hZOIFthHqDy7vJI++5t847lQedi/IdVkJLnl66kXDzGxie0yfm0Nx0oqy8Dbe07qO32NPUP" # Must be same as in app.py
pw = input("Password to be hashed: ")
md5_plus_salt = md5(pw.encode('utf-8')).hexdigest() + salt
salted = sha256(md5_plus_salt.encode('utf-8')).hexdigest()
print(salted)