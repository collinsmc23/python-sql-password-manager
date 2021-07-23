from hashlib import sha256
from Cryptodome.Cipher import AES 
from pbkdf2 import PBKDF2
import hashlib
from base64 import b64encode, b64decode


salt = b'.Y\x18\xcf\xe5\x044\x08'


def query_master_pwd(master_password, second_FA_location): 

    master_password_hash = "a6d8c9a7a3eda3fa56228a5ac3bf7157556de5bb74a2bcb6a0811caa01ccd665"

    compile_factor_together = hashlib.sha256(master_password + second_FA_location).hexdigest()

    if compile_factor_together == master_password_hash: 
        return True 
    
def encrypt_password(password_to_encrypt, master_password_hash): 
    
    key = PBKDF2(str(master_password_hash), salt).read(32)
    
    data_convert = str.encode(password_to_encrypt)

    cipher = AES.new(key, AES.MODE_EAX) 

    nonce = cipher.nonce

    ciphertext, tag = cipher.encrypt_and_digest(data_convert) 

    add_nonce = ciphertext + nonce

    encoded_ciphertext = b64encode(add_nonce).decode()

    return encoded_ciphertext

def decrypt_password(password_to_decrypt, master_password_hash): 
    
    if len(password_to_decrypt) % 4:
     
     password_to_decrypt += '=' * (4 - len(password_to_decrypt) % 4)

    convert = b64decode(password_to_decrypt)

    key = PBKDF2(str(master_password_hash), salt).read(32)

    nonce = convert[-16:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt(convert[:-16]) 

    return plaintext


