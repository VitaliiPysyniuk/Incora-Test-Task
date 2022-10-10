import re


def normalize_phone(phone: str) -> str:
    """
    Normalize user's phone number.

    Take validated user's phone number in different valid formats
    and parse it to the correct format to save the phone numbers
    of users in the DB in one unified format '+380xxxxxxxxx'.

    Parameters:
    phone (str): Validate user's phone number

    Returns:
    str: User's phone number in the correct format
    """
    phone_digits = ''.join(re.findall(r'[0-9]', phone))
    if len(phone_digits) != 12 and not phone_digits.startswith('38'):
        phone_digits = '38' + phone_digits
    correct_phone_format = '+' + phone_digits

    return correct_phone_format


