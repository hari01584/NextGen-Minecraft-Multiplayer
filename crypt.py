import hashlib
import os


def salt(salt,passw):
    key = hashlib.pbkdf2_hmac(
        'sha256', # The hash digest algorithm for HMAC
        passw.encode('utf-8'), # Convert the password to bytes
        salt.encode('utf-8'), # Provide the salt
        100000, # It is recommended to use at least 100,000 iterations of SHA-256 
        dklen=32 # Get a 128 byte key
    )
    return key.hex()
