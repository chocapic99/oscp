# Python For Offensive PenTest: A Complete Practical Course - All rights reserved 
# Follow me on LinkedIn  https://jo.linkedin.com/in/python2

# Download Pycrypto for Windows - pycrypto 2.6 for win32 py 2.7
# http://www.voidspace.org.uk/python/modules.shtml#pycrypto

# Download Pycrypto source
# https://pypi.python.org/pypi/pycrypto
# For Kali, after extract the tar file, invoke "python setup.py install"

import os
from Crypto.Cipher import AES


counter = os.urandom(16) #CTR counter string value with length of 16 bytes.
key = os.urandom(32)     #AES keys may be 128 bits (16 bytes), 192 bits (24 bytes) or 256 bits (32 bytes) long.


# Instantiate a crypto object called enc
enc = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
encrypted = enc.encrypt("Hussam"*5)
print encrypted


# And a crypto object for decryption
dec = AES.new(key, AES.MODE_CTR, counter=lambda: counter)
decrypted =  dec.decrypt(encrypted)
print decrypted

