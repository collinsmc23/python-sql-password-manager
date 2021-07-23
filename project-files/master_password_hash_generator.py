from hashlib import sha256
import hashlib

def master_password_gen(): 

    master_password = input("Enter your password: ").encode()

    compile_factor_together = hashlib.sha256(master_password).hexdigest()

    print("Master Password: " + str(compile_factor_together))

master_password_gen()
