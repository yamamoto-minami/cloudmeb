from Crypto.Cipher import AES
import base64
# import os

"""
Provides 2 methods for encrypting and decrypting stings.
sting Sting
encoded String
"""

PADDING = '{'
BLOCK_SIZE = 32
# SECRET = os.urandom(BLOCK_SIZE)
SECRET = b'R1\x85ZR\xe2\x12\r\xe2\xdaB\xca\xe4\xd1 \x96G\xa5\x06\xf6\xf5Iv\x14q\xb5\xb5\x88"\xbagI'
CIPHER = AES.new(SECRET)

pad = lambda string: string + (BLOCK_SIZE - len(string) % BLOCK_SIZE) * PADDING
encode_AES = lambda string: base64.b64encode(CIPHER.encrypt(pad(string)))
decode_AES = lambda endoded: CIPHER.decrypt(base64.urlsafe_b64decode(endoded)).decode('utf8').rstrip(PADDING)
