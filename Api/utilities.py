import string
import random


def serial_generator(size=6, chars=string.ascii_uppercase + string.digits):
    # function that generates a random serial number
    return ''.join(random.choice(chars) for _ in range(size))
