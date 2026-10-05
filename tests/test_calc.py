import pytest
from calc import apply_discount


def test_apply_discount_rejects_over_100():
    with pytest.raises(ValueError):
        apply_discount(100, 150)
    assert apply_discount(100, 100) == 0
