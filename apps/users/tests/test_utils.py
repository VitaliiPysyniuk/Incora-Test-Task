import pytest

from ..utils import normalize_phone


@pytest.mark.parametrize('phone_before,expected_phone', [
    ('+38(066)27-746-12', '+380662774612'),
    ('38(066)27-746-12', '+380662774612'),
    ('+3806627-746-12', '+380662774612'),
    ('380662774612', '+380662774612'),
    ('+06627-746-12', '+380662774612'),
    ('+0662774612', '+380662774612'),
    ('0662774612', '+380662774612')
])
def test_phone_normalization(phone_before, expected_phone):
    normalized_phone = normalize_phone(phone_before)

    assert type(normalized_phone) == str
    assert normalized_phone == expected_phone
