import secrets
import string

def password_gen(password_length):

    characters = string.ascii_letters + string.digits

    return ''.join(secrets.choice(characters) for _ in range(password_length))
