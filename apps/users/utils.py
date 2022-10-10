import re


def normalize_phone(phone: str) -> str:
    phone_digits = ''.join(re.findall(r'[0-9]', phone))
    if len(phone_digits) != 12 and not phone_digits.startswith('38'):
        phone_digits = '38' + phone_digits
    correct_phone_format = '+' + phone_digits

    return correct_phone_format


