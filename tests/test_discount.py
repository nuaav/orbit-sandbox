import pytest

from calc.discount import apply_discount


def test_apply_discount_raises_on_negative_percent():
    with pytest.raises(ValueError) as excinfo:
        apply_discount(100, -5)
    assert str(excinfo.value) == "Discount percent cannot be negative"
