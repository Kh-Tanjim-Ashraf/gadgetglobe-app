import random
import string



def random_alphanumeric(length=5):
    # Combine letters and digits (abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))