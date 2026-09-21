from calc.money import format_money


def test_format_money_usd():
    assert format_money(1234.5, "USD") == "$1,234.50"


def test_format_money_inr():
    assert format_money(1234.5, "INR") == "₹1,234.50"


def test_format_money_eur():
    assert format_money(1234.5, "EUR") == "€1,234.50"
