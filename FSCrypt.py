#!/usr/bin/python
from __future__ import print_function
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from base64 import decodestring
from base64 import encodestring
from sys import stdout
from sys import stdin

INITIALIZATION_VECTOR = b'tu89geji340t89u2'
PASSWORD = b'UGxheWVy'
encrypted_data = stdin.readline()

KEY_SIZE = 32

# Derive the key from our password and IV
key = PBKDF2(PASSWORD, INITIALIZATION_VECTOR, KEY_SIZE)

# Use AES in Block cipher mode with our key and IV 
aes_cbc_decryptor = AES.new(key, AES.MODE_CBC, INITIALIZATION_VECTOR)

message = decodestring(encrypted_data)

decrypted_data = aes_cbc_decryptor.decrypt(message)

for char in decrypted_data:
    # Don't print the padding characters (0c)
    if char == b'\x0c': break
    # Print each char to standard out
    stdout.write(char)