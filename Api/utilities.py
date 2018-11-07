import string
import random
import re


def serial_generator(size=6, chars=string.ascii_uppercase + string.digits):
    # function that generates a random serial number
    return ''.join(random.choice(chars) for _ in range(size))


def checks_empty_fields(*fields):
    """the function that checks for an empty field"""
    for field in fields:
        if field == "":
            return True


def check_field_types(parcel_name, description, pick_up, destination):
    """ function that checks if the types are string and it for price """
    if isinstance(parcel_name, str) and isinstance(description, str) and isinstance(pick_up, str) \
            and isinstance(destination, str):
        return True


def removes_white_spaces(name, description, pickup, destination):
    """function that removes white spaces from the field"""
    if not name.strip() and description.strip() and pickup.strip() and destination.strip():
        return True


def validate_status(status):
    """function that validates status"""
    if status != "pending" and status != "cancel" and status != "transit" and status != "Delivered":
        return True
