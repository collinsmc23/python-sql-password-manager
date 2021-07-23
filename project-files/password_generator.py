import secrets
import string

def password_gen(password_length):

    characters = string.ascii_letters + string.digits

    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))

    return secure_password
