import random

def generate_password(length=8):
    chars = "abc123"
    return "".join(random.choice(chars) for i in range(length))
