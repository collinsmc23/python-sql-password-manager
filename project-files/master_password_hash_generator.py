from hashlib import sha256
import hashlib

# Enter salt in ******* field. Salt must be in bytes.
salt = b'*******'

def master_password_gen(): 

    master_password = input("Enter your password: ").encode()

    compile_factor_together = hashlib.sha256(master_password).hexdigest()

    print("Master Password: " + str(compile_factor_together))

master_password_gen()
